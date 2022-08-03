# 13-1............ Navigate to command prompt, check PIP version available,
#                  and list all installed packages.
C:\Users\satyam agencies>pip install
WARNING: You are using pip version 22.0.4; however, version 22.2.1 is available.

C:\Users\satyam agencies> pip install --upgrade pip
Requirement already satisfied: pip in c:\users\satyam agencies\appdata\local\programs\python\python39-32\lib\site-packages (22.0.4)
Collecting pip
  Downloading pip-22.2.1-py3-none-any.whl (2.0 MB)
     ---------------------------------------- 2.0/2.0 MB 1.1 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.0.4
    Uninstalling pip-22.0.4:
      Successfully uninstalled pip-22.0.4

C:\Users\satyam agencies>pip list --outdated
Package                Version Latest  Type
---------------------- ------- ------- -----
asgiref                3.4.1   3.5.2   wheel
distlib                0.3.4   0.3.5   wheel
Django                 4.0     4.0.6   wheel
filelock               3.4.2   3.7.1   wheel
mysql-connector-python 8.0.29  8.0.30  wheel
Pillow                 9.0.0   9.2.0   wheel
platformdirs           2.4.1   2.5.2   wheel
pytz                   2021.3  2022.1  wheel
setuptools             58.1.0  63.4.0  wheel
tzdata                 2021.5  2022.1  wheel
virtualenv             20.12.1 20.16.2 wheel

C:\Users\satyam agencies>pip list --uptodate
Package  Version
-------- -------
pip      22.2.1
PyMySQL  1.0.2
six      1.16.0
sqlparse 0.4.2

