from random import *
d=dict(list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))+[(l[1],l[0]) for l in list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))])
i=input("Enter string to encode with a1z26: \n")
s=""
for c in i:
    if c in d: s+=str(d[c])
    else: s+=c
    s+=" "
print(s)