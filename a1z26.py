from random import *
import time
enum_list=list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))
enum_list.extend([(l[1],l[0]) for l in enum_list])
qs_answered, correct, time_limit = 0,0,15
start_time=time.time()
incorrect_list=[]
while time.time()-start_time<time_limit:
    c=choice(enum_list)
    print("\n"*20)
    print(str(c[0])+"\n")
    time_diff=time.time()-start_time
    print(f'You have {round(time_limit-time_diff,3)} seconds left')
    qs_answered+=1
    if input()==str(c[1]): correct+=1
    else: incorrect_list.append(c)
print("\n"*20)
print(f'After {time_limit} seconds, your average answer-per-second is {round(time_diff/qs_answered,3)}.')
print(f'You answered {correct}/{qs_answered} questions correctly.')
if incorrect_list:
    print("Here is a list of your missed words: ")
    for k,v in incorrect_list:
        print(str(k) +", "+str(v))