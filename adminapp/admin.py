from django.contrib import admin

# Register your models here.

from .models import (Student, Teacher, Parent, Subject, Address,
                     Student_Subject_Relation, Student_Teacher_Relation,
                     Subject_Teacher_Relation, Notification, Post)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Subject)
admin.site.register(Address)
# admin.site.register(Schedule)
# admin.site.register(Session)
admin.site.register(Student_Subject_Relation)
admin.site.register(Student_Teacher_Relation)
admin.site.register(Subject_Teacher_Relation)
admin.site.register(Notification)
admin.site.register(Post)
