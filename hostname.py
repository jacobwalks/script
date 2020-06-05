#!/usr/bin/python3

import os
import sys
import subprocess
import socket


# check what version of Java machine has --> java -version
# check if tomcat is running, if not start the service
# write the same script in shell """
def main():
    localhost = socket.gethostname()
    cwd = os.getcwd()

    print("\n The current IP is " + localhost)
    print("\n Current directory is " + cwd + "\n")
    java = subprocess.check_output(["java", "-version"])
    print(java)
    print("\n")
    tomcat = subprocess.check_output(["ps" ,"-ef", "|", "grep", "tomcat"])
    print(tomcat)

main()







