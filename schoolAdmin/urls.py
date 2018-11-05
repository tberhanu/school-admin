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
urlpatterns = [

    path('all-notifications/', views.AllNotifications.as_view(), name="all_notifications"),
    path('notification-details/<int:pk>/', views.NotificationDetails.as_view(), name="notification_details"),

    path('notifications/<int:level>/', views.Notice.as_view(), name='notifications'),

    path('staffs/', views.Staff.as_view(), name="staff"),
    path('', views.Home.as_view(), name='home'),
    path('send/', views.sending, name="send"),
    path('admin/', admin.site.urls, name="admin"),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

    path('grades/<int:studentid>/', views.Grade.as_view(), name="grades"),
    path('accounts/', include('allauth.urls')),
    # path('gitlog/', views.Homes.as_view(), name='homes'), # this couldn't work
    path('subject-details/<int:subjectid>/', views.SubjectDetail.as_view(), name="subject-details"),
    path('teacher-profile/<int:teacherid>/', views.TeacherProfile.as_view(), name="teacher_profile"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
