# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#s = 'zzaabcxhijqlmnoooxooooooooooo'
#s = 'abxcdefgaxayusdkslmnopqr'
#s = 'azcbobobegghakl'
#s = 'abcbcd'
#s = 'ktgzfzsxlvsjpfsh'
#s = 'zyxwvutsrqponmlkjihgfedcba'
s = 'grgvznlnrjavzxmryvedtmi'

s1, s2 = '', ''

for x in range(len(s)-1):
    if (s[x] < s[x+1:]):
        s1 += s[x]
        if len(s2) < len(s1):
            s2 = s1    
    else:
        s1 += s[x]
        if len(s2) < len(s1):
            s2 = s1
        s1 = ''
    
if len(s2) <= len(s1) and (s[len(s)-2] < s[len(s)-1]):
    print(s[len(s)-2],s[len(s)-1])
    s1 += s[len(s)-1]
    s2 = s1
    
print("Longest substring in alphabetical order is:", s2)