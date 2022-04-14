from random import *
import time
enum_list=list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))
enum_list.extend([(l[1],l[0]) for l in enum_list])
qs_answered, correct, time_limit = 0,0,30
start_time=time.time()
while time.time()-start_time<time_limit:
    c=choice(enum_list)
    print("\n"*20)
    print(str(c[0])+"\n")
    time_diff=time.time()-start_time
    print(f'You have {round(time_limit-time_diff,3)} seconds left')
    qs_answered+=1
    if input()==str(c[1]): correct+=1
    
print(f'After {time_limit} seconds, your average answers per second is ' 
    f'{round(time_diff/qs_answered,3)}, and you answered {correct}/{qs_answered} questions correctly.')