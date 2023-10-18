#!/usr/bin/env python
# coding: utf-8

import os
if not os.path.exists("reper"):
    os.mkdir("reper")

if os.path.exists("reper"):
    os.rmdir("reper")

filname = "mon_fichiers.txt"
if os.path.exists(filname):
    f = open(filname, "r")
    text = f.read()
    print(text)
    f.close()
else:
    print("fichier absent")



try:
    f = open(filname,"r")
except FileNotFoundError:
    print("ERREUR")
else:
    text = f.read()
    print(text)
    f.close()

