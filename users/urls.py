
from django.urls import path
from . import views
from django.conf.urls import url
# from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    ]
