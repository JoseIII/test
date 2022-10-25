from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from courses.forms import AddCourseForm, AddSectionForm, AddLessonForm
from courses.models import Course, Section, Lesson


def coursepage(request):
    courses = Course.objects.all()
    if request.user.is_authenticated:
        return render(request, "courses/courses.html", {'courses': courses})
    else:
        return redirect('loginpage')

def addcourse(request):
    form = AddCourseForm()
    if request.method == "POST":
        form = AddCourseForm(request.POST)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.ccreator = request.user
            print("PC")
            instance.save()
            return render(request, "courses/successcourse.html", {'form1': form})
    form = AddCourseForm()
    return render(request, "courses/addcourse.html", {'form': form})

def updatecourse(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, 'courses/editcoursehtml', context)

def updatecourserecord(request, id):
    course = Course.objects.get(id=id)
    form = AddCourseForm(request.POST, instance=course)
    if form.is_valid():
        form.save()
        return redirect("coursepage")

    return render(request, 'courses/editcourse.html', {'course':course})

def deletecourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("coursepage")

class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    template_name = "courses/detail.html"

def sectionspage(request):
    section = Section.objects.all()
    if request.user.is_authenticated:
        return render(request, "sections/sections.html", {'sections': section})
    else:
        return redirect('loginpage')

def addsections(request):
    if request.method == "POST":
        form = AddSectionForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "sections/successsections.html", {'form1': form})
    form = AddSectionForm()
    return render(request, "sections/addsections.html", {'form': form})

def updatesections(request, id):
    section = Section.objects.get(id=id)
    context = {
        'section': section
    }
    return render(request, 'sections/editsections.html', context)

def updatesectionsrecord(request, id):
    section = Section.objects.get(id=id)
    form = AddSectionForm(request.POST, instance=section)
    if form.is_valid():
        form.save()
        return redirect("sectionspage")

    return render(request, 'sections/editsections.html', {'section':section})

def deletesections(request, id):
    section = Section.objects.get(id=id)
    section.delete()
    return redirect("sectionspage")

def lessonpage(request):
    lesson = Lesson.objects.all()
    if request.user.is_authenticated:
        return render(request, "lessons/lessons.html", {'lessons': lesson})
    else:
        return redirect('loginpage')

def addlesson(request):
    if request.method == "POST":
        form = AddLessonForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "lessons/successlessons.html", {'form1': form})
    form = AddLessonForm()
    return render(request, "lessons/addlessons.html", {'form': form})

def deletelessons(request, id):
    lesson = Lesson.objects.get(id=id)
    lesson.delete()
    return redirect("lessonspage")