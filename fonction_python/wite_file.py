#!/usr/bin/env python
# coding: utf-8

f = open("mon_fichier.txt","w")
f.write("Bonjour\n")
l=[str(i)+"\n" for i in range(1,11)]
f.writelines(l)
f.close()