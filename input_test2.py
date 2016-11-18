#! /usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    var = raw_input()
    print ("input >>"+var)
    if var == "x":
        break
print("end")

#カンマ区切りで入力されたものを、上下・左右に分解して
#arduino側に渡すのを作る