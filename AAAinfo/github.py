"""
1. Deleting already pushed file to github, but not from the file
    schoolAdmin$ git rm --cached schoolAdmin/settings/sensitive_file.py
    schoolAdmin$ git commit -m "schoolAdmin/settings/sensitive_file.py"
    schoolAdmin$ git push (-f)* origin master
2. Deleting already pushed file both from the file and from the github
    schoolAdmin$ git rm sentisive_file_location_path.py
    schoolAdmin$ git commit -m "schoolAdmin/settings/sensitive_file.py"
    schoolAdmin$ git push (-f)* origin master
3. Add the full path of the sensitive_file you don't want to push to version control, github like:
    .gitignore --> schoolAdmin/settings/secured_info.py















"""
