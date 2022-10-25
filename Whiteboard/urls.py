"""Whiteboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from courses.views import coursepage, addcourse, deletecourse, updatecourse, updatecourserecord, CourseDetailView, \
    sectionspage, addsections, updatesections, updatesectionsrecord, deletesections, addlesson, lessonpage, \
    deletelessons
from accounts.views import RegisterView, loginpage
from .views import homepage, updaterecord, list_user, update, delete, myinfopage

from django.contrib.auth import views as logout

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name='homepage'),
    path('logout/', logout.LogoutView.as_view(template_name="auth/logout.html"), name='logoutpage'),
    path('login/', loginpage, name='loginpage'),
    path('register/', RegisterView.as_view(), name="registerpage"),
    path('admin/', admin.site.urls),
    path('infopage/', myinfopage ,name="myinfopage"),

    path('users/', list_user, name='list_user'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),

    path('course/', coursepage, name="coursepage"),
    path('course/<int:pk>', CourseDetailView.as_view(), name='detailed'),
    path('addcourse/', addcourse, name="addcoursepage"),
    path('editcourse/<int:id>', updatecourse, name="editcoursepage"),
    path('updatecourse/<int:id>', updatecourserecord, name="updatecourse"),
    path('deletecourse/<int:id>', deletecourse, name="deletecourse"),

    path('lessons', lessonpage, name="lessonspage"),
    path('lessons/addlessons', addlesson, name="addlessonspage"),
    path('deletelessons/<int:id>', deletelessons, name="deletelessons"),

    path('sections/', sectionspage, name="sectionspage"),
    path('addsections/', addsections, name="addsectionspage"),
    path('editsections/<int:id>', updatesections, name="editsectionspage"),
    path('updatesections/<int:id>', updatesectionsrecord, name="updatesections"),
    path('deletesections/<int:id>', deletesections, name="deletesections"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)