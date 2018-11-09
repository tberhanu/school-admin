from schoolAdmin.settings.base import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']


try:
    from schoolAdmin.settings.local import *
    EMAIL_USE_TLS = EMAIL_USE_TLS
    EMAIL_HOST = EMAIL_HOST
    EMAIL_HOST_USER = EMAIL_HOST_USER
    EMAIL_PORT = EMAIL_PORT
    EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD


    PASSWORD=PASSWORD
    SECRET_KEY=SECRET_KEY
except:
    pass
