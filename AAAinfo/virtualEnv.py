*Creating venv while there is already existed project called prev_project_name
0. prev_project_name tess$ pip unistall django
1. prev_project_name tess$ pythonX.Y -m venv someVEnv ,where X.Y is the python version you want
2. prev_project_name tess$ source someVEnv/bin/activate
3. (someVEnv)tess$pip install -r prev_project_name/requirements.dev.txt
4.               $python manage.py runserver
5.               $deactivate

*creating anther virtual environment
1. $pythonX.Y -m venv mysiteVEnv
2. $source mysiteVEnv/bin/activate
3. (mysiteVEnv)tess$ pip list
4. (mysiteVEnv)tess$ pip install django    --> will install latest django if version does not specified
5. (mysiteVEnv)tess$ django-admin startproject mysiteProject
6. (mysiteVEnv)tess$ cd mysiteProject
7. (mysiteVEnv):mysiteProject tess$ python manage.py runserver


N.B.*** Avoid using Environmental Variables for the SECRET_KEY, PASSWORD, DJANGO_SETTINGS_MODULE etc
        as it creates confusion among different venvs. For now, I stored SECRET_KEY and PASSWORD
        inside the secured_info.py which is a .gitignored file. Plus I just avoided to use different
        settings like dev, prod, and base.py so that I don't need to have a DJANGO_SETTINGS_MODULE
        to be stored as an environmental variable. But I need also to figure out where I should save
        and use this too.
