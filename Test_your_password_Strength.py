# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:26:41 2019

@author: SAM
"""
file=open('Passwordstats.txt','w')
a=1
percentofsp=0
percentofcaps=0
specialcharcount=0
capscount=0
Score=0
l=list(range(33,65))
caps=list(range(65,90))
print("--------Welcome to Password rating program---------")
print("------Check out how strong is your Password-------")
while(a==1):
    Password=input("Please enter the desired Password: ")
    if(len(Password)>8):
        a=0
for i in Password:
    if ord(i) in l:
        specialcharcount=specialcharcount+1
        percentofsp=len(Password)*100/specialcharcount
for ii in range(0,len(Password)):
    
    if (ord(Password[ii]) in l) & (ord(Password[ii-1]) in l):
        strength=specialcharcount-0.5
    else:
        strength=specialcharcount+1
for i in Password:
    if ord(i) in caps:
        capscount=capscount+1
        percentofcaps=len(Password)*100/capscount
score=strength+capscount
if score>5 & score<10:
    d='Can do better, special characters and numbers are {0} % of the Password and {1} % are Caps'
    print(d.format(percentofsp,percentofcaps))
if score>10 & score<15:
    d='Good Password, Special Charcaters are also nicely assigned, special characters and numbers are {0} % of the Password {1} % are Caps'
    print(d.format(percentofsp,percentofcaps))
if score>15:
    d='Great Password better write it down, special characters and numbers are {0} % of the Password and {1} % are caps'
    print(d.format(percentofsp,percentofcaps))
if score <5 :
    d='Bad password I can also guess hmmm ur password is {2}, special characters and numbers are {0} % of the Password and {1} %are caps'
    print(d.format(percentofsp,percentofcaps,Password))
choice=input("Do you want a text copy of stats and tests done on your Password and score report then Press Y for YES and N for a NO :")
if choice=='YES':
    file.write("Thank you I'm sleepy will write your stats later bye")
