from random import *
import time
letters = "abcdefghijklmnopqrstuvwxyz"
letters_list=list(letters)
enum_list=list(enumerate(letters_list,1))

letter_first = [(l[1],l[0]) for l in enum_list]
enum_list.extend(letter_first)
start_time=time.time()
qs_answered=0
correct=0
while True:
    c=choice(enum_list)
    print(c[0])
    i=input()
    qs_answered+=1
    if i==str(c[1]):
        print("correct")
        correct+=1
    else:
        print("incorrect")
    time_diff=time.time()-start_time
    print(f'You take {time_diff/qs_answered} seconds on average')
