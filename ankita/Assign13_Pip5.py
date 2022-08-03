# 13-5.......... Using pip install package from local tar and wheel files.

C:\Users\satyam agencies>pip install -U wheel files
Requirement already satisfied: wheel in c:\users\satyam agencies\appdata\local\programs\python\python39-32\lib\site-packages (0.37.1)
Collecting files
  Downloading files-1.1.1.tar.gz (10 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: files
  Building wheel for files (setup.py) ... done
  Created wheel for files: filename=files-1.1.1-py3-none-any.whl size=3649 sha256=a5465d14d10d56fc920b3b34d7d25ebcf1dc9172bf0fb3788981448ec211fb7b
  Stored in directory: c:\users\satyam agencies\appdata\local\pip\cache\wheels\a3\80\ef\3100c2c6092a3e8fb607675e024bd724fefc5b3979f8f062a4
Successfully built files
Installing collected packages: files
Successfully installed files-1.1.1

C:\Users\satyam agencies>pip list wheel files
Package                Version
---------------------- -------
asgiref                3.4.1
distlib                0.3.4
Django                 4.0
filelock               3.4.2
files                  1.1.1
mysql-connector-python 8.0.29
Pillow                 9.0.0
pip                    22.2.1
platformdirs           2.4.1
PyMySQL                1.0.2
pytz                   2021.3
setuptools             63.4.0
six                    1.16.0
sqlparse               0.4.2
tzdata                 2021.5
virtualenv             20.12.1
wheel                  0.37.1
