from random import *
letter_to_num=dict(list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1)))
num_to_letter=dict([(l[1],l[0]) for l in list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))])
d=letter_to_num+num_to_letter
def convert_a1z26(i):
    s=""
    for c in i:
        if c in letter_to_num: s+=str(d[c])
        else: s+=c
        s+=" "
    return s
i=input("Enter string to encode with a1z26: \n")
s=convert_a1z26(i)
print(s)