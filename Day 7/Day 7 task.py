#DAY 7 TASK
#1)Create a python module with list and import the module in another .py file and change the value in list

import my_module as mm
print(mm.my_list)
mm.my_list[0] = 6
print(mm.my_list)

#2)Install pandas package (try to import the package in a python file)

#Installed succesfully

Collecting pandas
  Downloading pandas-1.1.4-cp39-cp39-win_amd64.whl (8.9 MB)
     |████████████████████████████████| 8.9 MB 108 kB/s
Requirement already satisfied: python-dateutil>=2.7.3 in c:\users\user\appdata\local\programs\python\python39\lib\site-p
ackages (from pandas) (2.8.1)
Collecting numpy>=1.15.4
  Downloading numpy-1.19.4-cp39-cp39-win_amd64.whl (13.0 MB)
     |████████████████████████████████| 13.0 MB 819 kB/s
Collecting pytz>=2017.2
  Downloading pytz-2020.4-py2.py3-none-any.whl (509 kB)
     |████████████████████████████████| 509 kB 233 kB/s
Requirement already satisfied: six>=1.5 in c:\users\user\appdata\local\programs\python\python39\lib\site-packages (from
python-dateutil>=2.7.3->pandas) (1.15.0)
Installing collected packages: numpy, pytz, pandas
Successfully installed numpy-1.19.4 pandas-1.1.4 pytz-2020.4

#3)Import a module that picks random number and write a program to fetch a random number from 1 to 100 on every run

import random
print("Random number from 1 to 100 is",random.randint(1,100))

#4)Import sys package and find the python path


import sys
sys.path

['', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\win32', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\win32\\lib', 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\Pythonwin']

#5)Try to install and uninstall a package

pip uninstall pandas
