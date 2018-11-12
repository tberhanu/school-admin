"""schoolAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import ArticleDetailView
from django.conf.urls import url

from django.contrib.auth.views import password_reset_confirm
# app_name = 'adminapp'
urlpatterns = [
    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'registration/reset_password_confirm.html'}, name='password_reset_confirm'),
    path('logout_message/', views.logout_message),
    path('login_message/', views.login_message),
    path('users/', include('users.urls')), # we customize this for 'sign up' purpose
    path('users/', include('django.contrib.auth.urls')),

    path('all-notifications/', views.AllNotifications.as_view(), name="all_notifications"),
    path('notification-details/<int:pk>/', views.NotificationDetails.as_view(), name="notification_details"),

    path('notifications/<int:level>/', views.Notice.as_view(), name='notifications'),

    path('staffs/', views.Staff.as_view(), name="staff"),
    path('', views.Home.as_view(), name='home'),
    path('send/', views.sending, name="send"),
    path('admin/', admin.site.urls, name="admin"),




    path('grades/<int:studentid>/', views.Grade.as_view(), name="grades"),
    path('subject-details/<int:subjectid>/', views.SubjectDetails.as_view(), name="subject-details"),
    path('teacher-profile/<int:teacherid>/', views.TeacherProfile.as_view(), name="teacher_profile"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
