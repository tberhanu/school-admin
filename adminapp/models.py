from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import datetime
from django.conf import settings

# Create your models here.
class Address(models.Model):
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    apt = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return "Phone: " + self.phone
    def __repr__(self):
        return "Phone: " + self.phone

class Parent(models.Model):

    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_email = models.EmailField(max_length=254, blank=True)
    mother_email = models.EmailField(max_length=254, blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return "Parent: " + self.father_name + " and " + self.mother_name
    def __repr__(self):
        return self.father_name + " and " + self.mother_name

class Subject(models.Model):
    subjectid = models.BigIntegerField(primary_key = True)

    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=30, blank=True)
    course_number = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title

class Teacher(models.Model):
    teacherid = models.BigIntegerField(primary_key = True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    credentials = models.CharField(max_length=100, blank=True)
    subjects = models.ManyToManyField(Subject, through='Subject_Teacher_Relation', blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    def __repr__(self):
        return self.first_name + " " + self.last_name

class Student(models.Model):
    studentid = models.BigIntegerField(primary_key = True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # new
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    level = models.IntegerField()
    gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE, blank=True)
    subjects = models.ManyToManyField(Subject, through='Student_Subject_Relation', blank=True)
    teachers = models.ManyToManyField(Teacher, through='Student_Teacher_Relation', blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    def __repr__(self):
        return self.first_name + " " + self.last_name

class Student_Subject_Relation(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, blank=True)
    semester = models.CharField(max_length=30, blank=True)
    grade = models.CharField(max_length=4, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Student_Subject: " + self.student.first_name + " " + self.subject.title
    def __repr__(self):
        return self.student.first_name + " " + self.subject.title

class Student_Teacher_Relation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, blank=True)
    semester = models.CharField(max_length=30, blank=True)
    level = models.CharField(max_length=30, blank=True)
    teacher_comment = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return "Student_Teacher: " + self.student.first_name + " " + self.teacher.first_name
    def __repr__(self):
        return self.student.first_name + " " + self.teacher.first_name


class Subject_Teacher_Relation(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, blank=True)
    semester = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "Subject_Teacher: " + self.subject.title + " " + self.teacher.first_name
    def __str__(self):
        return self.subject.title + " " + self.teacher.first_name

class Notification(models.Model):
    title = models.CharField(max_length=30)
    course = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True)
    level = models.CharField(max_length=30, blank=True)
    poster = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='notification_image', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def __str__(self):
        return self.title

# class Chat(models.Model):
#     post = models.CharField(max_length=500)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
