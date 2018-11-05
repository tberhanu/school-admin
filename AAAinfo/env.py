"""
1. Setting Environmental Variable PERMANENTLY
    --> tess$ cd    #to stay on our HOME DIRECTORY
    --> tess$ touch .bash_profile #just updating the last access time for that files
    --> tess$ cp .bash_profile .bash_profile_BACKUP #just copying a backup file
    --> tess$ open -a "Brackets" .bash_profile
        --> export SECRET_KEY="asldvnkaadfhdfaj862435dfnsfsfdadsl"
        --> Save it and CLOSE OUT of the terminal, then
        --> tess$ echo $SECRET_KEY #Should give you back whatever you've saved.DONE.
2. Setting Environmental Variable TEMPORARILY
    --> schoolAdmin$ export DJANGO_SETTINGS_MODULE=schoolAdmin.settings.dev
3. After changing the SETTINGS file location, Django may get confused and raise errors like
    The SECRET_KEY setting must not be empty. So, telling Django the location is like
    --> schoolAdmin$ python manage.py runserver --settings=schoolAdmin.settings.dev
4. PERMANENTLY telling Django telling the new SETTINGS file location:
    ---> Repeat step# 1 and --> export DJANGO_SETTINGS_MODULE="schoolAdmin.settings.dev"
    then CLOSE OUT OF TERMINAL, then --> $python manage.py runserver
































"""
