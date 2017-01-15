#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 02:43:34 2017

@author: drew
"""
s = 'azcbobobegghakl'
bob = 0
index = 0
for count in s:
    if index >= 2 and s[index-2] == 'b' and s[index-1] == 'o' and s[index] == 'b':
       bob += 1
    index += 1
print("Number of times bob occurs is: ", bob)