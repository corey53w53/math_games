from random import *
letter_to_num=dict(list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1)))
num_to_letter=dict([(str(l[1]),l[0]) for l in list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))])
d=letter_to_num+num_to_letter
def convert_to_a1z26(i):
    s=""
    for c in i:
        if c in letter_to_num: s+=str(d[c])
        else: s+=c
        s+=" "
    return s
def convert_to_num(i):
    s=""
    i=i.split()
    print(i)
    for c in i:
        if c in num_to_letter: s+=str(d[c])
        else: s+=c
        s+=" "
    return s
i=input("Enter string to encode with a1z26: \n")
i="12 13 14 7"
s=convert_to_num(i)
print(s)