import random as r
from itertools import permutations
def all_operators(num1,num2):
    list=[num1+num2,num1-num2,num1*num2]
    if num2: list.append(num1/num2)
    return list
def branch(num,l):
    new_l=[]
    for value in l: new_l+=all_operators(num,value)
    return new_l
def possible_solutions(base_list):
    total_list=[]
    all_lists=permutations(base_list)
    for current_list in all_lists:
        current_branch=[current_list[0]]
        for num in current_list[1:]: current_branch+=branch(num,current_branch) 
        total_list+=current_branch
        first_two_list=all_operators(current_list[0],current_list[1])
        second_two_list=all_operators(current_list[2],current_list[3])
        for number in first_two_list: total_list+=branch(number,second_two_list)
        for number in second_two_list: total_list+=branch(number,first_two_list)
    return sorted(list(set(total_list)))
def twenty_four_can_be_made(input_list):
    total_list=possible_solutions(input_list)
    return 24 in total_list
while True:
    l=[0,0,0,0]
    while not twenty_four_can_be_made(l):
        l=[]
        for _ in range(4):
            l.append(r.randint(1,13))
    print(l,end="")
    input()
#TODO somehow print solution? ugh