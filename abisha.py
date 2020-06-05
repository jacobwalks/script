#!/usr/bin/python3

import os
import sys


def main():
    print("\n")
    cwd = os.getcwd()
    print(cwd)
    foldername = "walk"
    if foldername == "walk":
        os.mkdir(foldername)
        print("\n")
    else:
        print("Folders name is invalid, exiting script")


def checkingfolder():
    print("print this from the second function")
    cwd, foldername = main()
    newpath = '/home/ubuntu/script/walk'
    isdir = os.path.isdir(newpath)

    if (isdir == True):
        print("Folder named " + foldername + " has been created in " + cwd)
    else:
        print("Folders name is invalid, exiting script")
    print("\n")


main()
