from django import forms
from django.forms import fields
from courses.models import Course, Section, Lesson

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class AddSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"

class AddLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"