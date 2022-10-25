from django.db import models
from accounts.models import User

class Section(models.Model):
    nameofsection = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.nameofsection

class Course(models.Model):
    ctitle = models.CharField(max_length=50, default="")
    cdescription = models.TextField(max_length=200, default="")
    ccreator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    #csection = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.ctitle

    def __unicode__(self):
        return self.ctitle

    class Meta:
        db_table="courses"

class Lesson(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField(max_length=200, default="")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title