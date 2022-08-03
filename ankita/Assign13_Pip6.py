# 13-6.......... Uninstall all installed packages and make sure to clean the environment.

C:\Users\satyam agencies>pip install virtualenv
Requirement already satisfied: virtualenv in c:\users\satyam agencies\appdata\local\programs\python\python39-32\lib\site-packages (20.12.1)
Requirement already satisfied: six<2,>=1.9.0 in c:\users\satyam agencies\appdata\local\programs\python\python39-32\lib\site-packages (from virtualenv) (1.16.0)
Requirement already satisfied: distlib<1,>=0.3.1 in c:\users\satyam agencies\appdata\local\programs\python\python39-32\lib\site-packages (from virtualenv) (0.3.4)
Requirement already satisfied: filelock<4,>=3.2 in c:\users\satyam agencies\appdata\local\programs\python\python39-32\lib\site-packages (from virtualenv) (3.4.2)
Requirement already satisfied: platformdirs<3,>=2 in c:\users\satyam agencies\appdata\local\programs\python\python39-32\lib\site-packages (from virtualenv) (2.4.1)


C:\Users\satyam agencies>virtualenv MyEnv
created virtual environment CPython3.9.13.final.0-32 in 26337ms
  creator CPython3Windows(dest=C:\Users\satyam agencies\MyEnv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\satyam agencies\AppData\Local\pypa\virtualenv)
    added seed packages: pip==21.3.1, setuptools==60.2.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator


C:\Users\satyam agencies>MyEnv/scripts
'MyEnv' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\satyam agencies>MyEnv/scripts/activate
'MyEnv' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\satyam agencies>MyEnv\scripts\activate


(MyEnv) C:\Users\satyam agencies>pip install django
Collecting django
  Downloading Django-4.1-py3-none-any.whl (8.1 MB)
     |████████████████████████████████| 8.1 MB 1.1 MB/s
Collecting asgiref<4,>=3.5.2
  Downloading asgiref-3.5.2-py3-none-any.whl (22 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting tzdata
  Downloading tzdata-2022.1-py2.py3-none-any.whl (339 kB)
     |████████████████████████████████| 339 kB 726 kB/s
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.2 django-4.1 sqlparse-0.4.2 tzdata-2022.1
WARNING: You are using pip version 21.3.1; however, version 22.2.1 is available.
You should consider upgrading via the 'C:\Users\satyam agencies\MyEnv\Scripts\python.exe -m pip install --upgrade pip' command.

(MyEnv) C:\Users\satyam agencies>pip  freeze
asgiref==3.5.2
Django==4.1
sqlparse==0.4.2
tzdata==2022.1

(MyEnv) C:\Users\satyam agencies>pip  freeze > requirements.txt


(MyEnv) C:\Users\satyam agencies>pip uninstall -r requirements.txt
Found existing installation: asgiref 3.5.2
Uninstalling asgiref-3.5.2:
  Would remove:
    c:\users\satyam agencies\myenv\lib\site-packages\asgiref-3.5.2.dist-info\*
    c:\users\satyam agencies\myenv\lib\site-packages\asgiref\*
      
Proceed (Y/n)? y
  Successfully uninstalled asgiref-3.5.2
Found existing installation: Django 4.1
Uninstalling Django-4.1:
  Would remove:
    c:\users\satyam agencies\myenv\lib\site-packages\django-4.1.dist-info\*
    c:\users\satyam agencies\myenv\lib\site-packages\django\*
    c:\users\satyam agencies\myenv\scripts\django-admin.exe
      
Proceed (Y/n)? y
  Successfully uninstalled Django-4.1
Found existing installation: sqlparse 0.4.2
Uninstalling sqlparse-0.4.2:
  Would remove:
    c:\users\satyam agencies\myenv\lib\site-packages\sqlparse-0.4.2.dist-info\*
    c:\users\satyam agencies\myenv\lib\site-packages\sqlparse\*
    c:\users\satyam agencies\myenv\scripts\sqlformat.exe
      
Proceed (Y/n)? y
  Successfully uninstalled sqlparse-0.4.2
Found existing installation: tzdata 2022.1
Uninstalling tzdata-2022.1:
  Would remove:
    c:\users\satyam agencies\myenv\lib\site-packages\tzdata-2022.1.dist-info\*
    c:\users\satyam agencies\myenv\lib\site-packages\tzdata\*
      
Proceed (Y/n)? y
  Successfully uninstalled tzdata-2022.1

(MyEnv) C:\Users\satyam agencies>pip freeze

(MyEnv) C:\Users\satyam agencies>deactivate
