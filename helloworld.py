#!/usr/bin/python3
import subprocess
#import subprocess as sp -> instead writing subprovess all the time we can just write it as sp
import os
import sys
from datetime import date
import getpass

print("\n")
today = date.today()
print("Today's date:", today)

print("\n")
x = "HelloWorld !!"
print (x)
print("\n")

print("\n")
java = subprocess.check_output(["java", "-version"]).decode('utf-8')
print (java)
print("\n")

python = subprocess.check_output(["python", "--version"]).decode('utf-8')
print (python)
print("\n")

ansible = subprocess.check_output(["ansible", "--version"]).decode('utf-8')
print(ansible)
print("\n")

git = subprocess.check_output(["git", "--version"]).decode('utf-8')
print(git)
print("\n")

mysql = subprocess.check_output(["mysql", "--version"]).decode('utf-8')
print(mysql)
print("\n")

"""
disk = subprovess.check_output(["df", "-h"])
print(disk)
print("\n") 
"""

whoami = subprocess.check_output(["whoami"]).decode('utf-8')
print( whoami)
"""
root = subprocess.check_output(["sudo", "-kS"]).decode('utf-8')

username = getpass.getuser()
print(username)


maven = subprocess.check_output(["mvn", "-version"]).decode('utf-8')
print (maven)
print("\n")

tomcat = subprocess-check_output(["./home/ubuntu/tomcat/bin/version.sh"]).decode('utf-8')
print(tomcat)
print("\n")
"""
