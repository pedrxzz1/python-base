#!/usr/bin/env python3
import os
import sys

# LBYL - Look Befero You Leap

if os.path.exits("names.txt"):
    print("o arquivo existe")
    input("...")   # Race Condition
    names = open("names.txt").readline()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1) 


if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
       
