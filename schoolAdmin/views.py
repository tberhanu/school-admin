from django.shortcuts import render, redirect, HttpResponseRedirect
from adminapp.models import (Student, Student_Subject_Relation, Subject,
 Subject_Teacher_Relation, Teacher, Notification, Post)
from django.shortcuts import get_object_or_404
# myproject/views.py
from django.views.generic import TemplateView
from django.conf import settings

# from django.core.mail import EmailMessage
from django.core.mail import send_mail
from adminapp.forms import HomeForm
def sending(request):
    # email = EmailMessage('title', 'body', to=['tberhanu@berkeley.edu'])
    # email.send()

    send_mail(
    'Subject here',
    'Here is the message.',
    'tesfahunt@gmail.com',
    ['tesfahunt@bisrategabriel.com', 'tberhanu@berkeley.edu', 'tessberhanu@gmail.com', 'tesfahunt@gmail.com'],
    fail_silently=False,)
    return render(request, 'adminapp/send.html')


class Home(TemplateView):
    template_name = 'adminapp/home.html'

def logout(request):
    return render(request, 'registration/logout.html')

class Grade(TemplateView):
    template_name = 'adminapp/grades.html'
    def get(self, request, studentid=None):
        login_url = settings.LOGIN_URL.lstrip('/')
        """ Omitting the following 'IfCase', still protected but not returning 404,
        rather error message telling Anonymous User don't have such Attribute"""
        if not request.user.is_authenticated:
            return redirect(login_url)
        else:
            if request.user.student.studentid != studentid:
                return redirect(login_url)
            else:
                student = Student.objects.get(studentid=studentid)
                subjects = student.subjects.all()
                relationships = []
                for subject in subjects:
                    relationships = relationships + [get_object_or_404(Student_Subject_Relation, student=student, subject=subject)]

                args = {'relationships': relationships}
                return render(request, self.template_name, args)

class SubjectDetail(TemplateView):
    template_name = 'adminapp/subject_details.html'
    def get(self, request, subjectid):
        login_url = settings.LOGIN_URL.lstrip('/')
        if not request.user.is_authenticated:
            return redirect(login_url)
        else:
            subject = Subject.objects.get(subjectid=subjectid)
            relationships = Subject_Teacher_Relation.objects.filter(subject=subject)
            args = {'subject': subject, 'relationships': relationships}
            return render(request, self.template_name, args)

class TeacherProfile(TemplateView):
    template_name = 'adminapp/teacher_profile.html'
    def get(self, request, teacherid):
        login_url = settings.LOGIN_URL.lstrip('/')
        if not request.user.is_authenticated:
            return redirect(login_url)
        else:
            teacher = Teacher.objects.get(teacherid=teacherid)
            args = {'teacher': teacher}
            return render(request, self.template_name, args)

class Staff(TemplateView):
    template_name = 'adminapp/staffs.html'
    def get(self, request):
        teachers = Teacher.objects.all().order_by('first_name')
        args = {'teachers': teachers}
        return render(request, self.template_name, args)

class Notice(TemplateView):
    template_name = 'adminapp/notifications.html'
    def get(self, request, level):
        login_url = settings.LOGIN_URL.lstrip('/')
        if not request.user.is_authenticated:
            return redirect(login_url)
        notifications = Notification.objects.all().filter(level=level).order_by('-pub_date')
        args = {'notifications': notifications}
        return render(request, self.template_name, args)
        
class AllNotifications(TemplateView):
    template_name = 'adminapp/all_notifications.html'
    def get(self, request):
        login_url = settings.LOGIN_URL.lstrip('/')
        if not request.user.is_authenticated:
            return redirect(login_url)
        notifications = Notification.objects.all().order_by('-pub_date', 'level')
        args = {'notifications': notifications}
        return render(request, self.template_name, args)

class NotificationDetails(TemplateView):
    template_name = 'adminapp/notification_details.html'
    def get(self, request, pk):
            form = HomeForm()
            notification = Notification.objects.get(id=pk)
            posts = Post.objects.filter(notification=notification).all().order_by('-created')
            args = {'form': form, 'posts': posts, 'notification': notification}
            return render(request, self.template_name, args)

    def post(self, request, pk):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            notification = Notification.objects.get(id=pk)

            post.student = request.user.student
            post.notification = notification
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('/notification-details/%d/' % pk)

        args = {'form': form, 'text': text, 'notification': notification}
        return render(request, self.template_name, args)
