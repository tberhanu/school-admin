
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),

    url(r'^change-password/$', views.change_password, name='change_password'),
    # url(r'^reset-passsword/$', password_reset, name='reset_password'),
    # url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete')


    ]
