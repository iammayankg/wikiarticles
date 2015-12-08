# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 17:42:31 2015

@author: Mayank
"""
def permute_words (text, n):
    import random
    text=text.replace("\n","")
    words=text.split(" ")
    l = len(words)
    if l <=2:
        print words
        return []
    perms=[]
    count=0;
    print(text)
    while count < n:
        x=random.randint(0,l-1)
        y=random.randint(0,l-1)
        if x==y:
            continue
        print(x,y)
        words[x],words[y] = words[y],words[x]
        perms.append(" ".join(words))
        words[x],words[y] = words[y],words[x]
        count += 1
    return perms
f=open("randomsentences.txt","r")
for line in f:
    #print(line)
    print(permute_words(line,1))

import subprocess
o=subprocess.check_output("echo 143",shell=True)
print(float(o),type(o))