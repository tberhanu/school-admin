"""The following information need to be double checked"""
Instead of using ENVIRONMENTAL VARIABLE, here is also anther option to save sensitive info:
1. Put the variables in schoolAdmin/settings/secured_info.py and add this file to our .gitignore file
2. Then we import this file whenever we want to access those variables like in base.py file:
--> from .secured_info import * # new
--> from schoolAdmin.settings import secured_info
--> PASSWORD = secured_info.PASSWORD
--> EMAIL_HOST_USER = secured_info.EMAIL_HOST_USER
--> EMAIL_HOST_PASSWORD = secured_info.EMAIL_HOST_PASSWORD
