#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 02:46:31 2017

@author: drew
"""
s = 'azcbobobegghakl'
vowels = 0
for count in s:
    if count == 'a' or count == 'e' or \
    count == 'i' or count == 'o' or count == 'u':
        vowels += 1
print("Number of vowels: ", vowels)