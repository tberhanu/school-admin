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


class Homes(TemplateView):
    template_name = 'homes.html'


def home(request):
    return render(request, 'adminapp/home.html')
def logout(request):
    return render(request, 'registration/logout.html')

def grades(request, studentid=None):
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
            return render(request, 'adminapp/grades.html', args)

def subject_details(request, subjectid=None):
    login_url = settings.LOGIN_URL.lstrip('/')
    if not request.user.is_authenticated:
        return redirect(login_url)
    else:
        subject = Subject.objects.get(subjectid=subjectid)
        relationships = Subject_Teacher_Relation.objects.filter(subject=subject)
        args = {'subject': subject, 'relationships': relationships}
        return render(request, 'adminapp/subject_details.html', args)

def teacher_profile(request, teacherid=None):
    login_url = settings.LOGIN_URL.lstrip('/')
    if not request.user.is_authenticated:
        return redirect(login_url)
    else:
        teacher = Teacher.objects.get(teacherid=teacherid)
        args = {'teacher': teacher}
        return render(request, 'adminapp/teacher_profile.html', args)

def staffs(request):
    teachers = Teacher.objects.all().order_by('first_name')
    args = {'teachers': teachers}
    return render(request, 'adminapp/staffs.html', args)

def notifications(request, level=None):
    login_url = settings.LOGIN_URL.lstrip('/')
    if not request.user.is_authenticated:
        return redirect(login_url)
    notifications = Notification.objects.all().filter(level=level).order_by('-pub_date')
    args = {'notifications': notifications}
    return render(request, 'adminapp/notifications.html', args)
def notification_details(request, pk=None):
    login_url = settings.LOGIN_URL.lstrip('/')
    if not request.user.is_authenticated:
        return redirect(login_url)
    else:
        notification = Notification.objects.get(id=pk)
        args = {'notification': notification}
        return render(request, 'adminapp/notification_details.html', args)
def all_notifications(request):
    login_url = settings.LOGIN_URL.lstrip('/')
    if not request.user.is_authenticated:
        return redirect(login_url)
    notifications = Notification.objects.all().order_by('-pub_date', 'level')
    args = {'notifications': notifications}
    return render(request, 'adminapp/all_notifications.html', args)

class NotificationDetails(TemplateView):
    template_name = 'adminapp/notification_details.html'
    def get(self, request, pk):
            form = HomeForm()
            notification = Notification.objects.get(id=pk)
            posts = Post.objects.filter(notification=notification).all().order_by('-created')
            # users = User.objects.exclude(id=request.user.id)
            # friend = Friend.objects.get(current_user=request.user)
            # friends = friend.users.all()

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
