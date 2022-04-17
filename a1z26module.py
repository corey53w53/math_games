from random import *
import time

def randq():
    return choice(list(dict(list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))+[(l[1],l[0]) for l in list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))]).items()))
print(randq())
d=dict(list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))+[(l[1],l[0]) for l in list(enumerate(list("abcdefghijklmnopqrstuvwxyz"),1))])
i="corey wang"
s=""
for c in i:
    if c in d:
        s+=str(d[c])
    else:
        s+=c
    s+=" "
print(s)


# time_limit=15
# start_time=time.time()
# while time.time()-start_time<time_limit:
#     c=choice(list(enum_list.items()))
#     print("\n"*20)
#     print(str(c[0])+"\n")
#     time_diff=time.time()-start_time
#     print(f'You have {round(time_limit-time_diff,2)} seconds left')
#     if input()==str(c[1]) and time.time()-start_time<time_limit: correct+=1
#     elif time.time()-start_time<time_limit: incorrect_list.append(c)
#     if time.time()-start_time<time_limit: qs_answered+=1
# print("\n"*20)
# if qs_answered: print(f'After {time_limit} seconds, your average answer-per-second is {round(time_diff/qs_answered,3)}.')
# if correct: print(f'Your average correct-answer-per-second is {round(time_diff/correct,3)}.')
# print(f'You answered {correct}/{qs_answered} questions correctly.')
# if incorrect_list:
#     print("Here are your incorrect answers: ")
#     for k,v in incorrect_list:
#         print(str(k) +" -> "+str(v))