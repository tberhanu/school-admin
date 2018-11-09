from schoolAdmin.settings.base import *

DEBUG = False


try:
    from schoolAdmin.settings.local import *
except:
    pass
