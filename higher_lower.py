import random as r

def calc_tries(highest_possible_num):
    final=1
    counter=0
    while final<highest_possible_num:
        final*=2
        counter+=1
    return counter
    
    highest_possible_num

difficulty=input("Enter your difficulty (1-3)\n")
difficulty=int(difficulty)
if difficulty==3:
    highest_num=1000
elif difficulty==2:
    highest_num=500
elif difficulty==1:
    highest_num=100
answer=r.randint(1,highest_num)
tries=calc_tries(highest_num)
handicap=3-difficulty
tries+=handicap
print(tries)
print(f'I have picked a number from 1 to {highest_num}')
while tries>0:
    guess=int(input("Enter your guess:\n"))
    tries-=1
    if guess==answer:
        print("You win!")
        exit()
    elif guess<answer:
        print("Your guess was too low")
    elif guess>answer:
        print("Your guess was too high")
    print(f'You have {tries} guesses left')