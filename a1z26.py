from random import *
import time
enum_list=list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))
enum_list.extend([(l[1],l[0]) for l in enum_list])
qs_answered, correct, time_limit = 0,0,3
start_time=time.time()
incorrect_list=[]
while time.time()-start_time<time_limit:
    c=choice(enum_list)
    print("\n"*20)
    print(str(c[0])+"\n")
    time_diff=time.time()-start_time
    print(f'You have {round(time_limit-time_diff,2)} seconds left')
    if input()==str(c[1]):
        if time.time()-start_time<time_limit: 
            correct+=1
            qs_answered+=1
    else: 
        if time.time()-start_time<time_limit: 
            qs_answered+=1
            incorrect_list.append(c)
    time_diff=time.time()-start_time
print("\n"*20)
if qs_answered: print(f'After {time_limit} seconds, your average answer-per-second is {round(time_diff/qs_answered,3)}.')
if correct: print(f'Your average correct-answer-per-second is {round(time_diff/correct,3)}.')
print(f'You answered {correct}/{qs_answered} questions correctly.')
if incorrect_list:
    print("Here are your incorrect answers: ")
    for k,v in incorrect_list:
        print(str(k) +" -> "+str(v))