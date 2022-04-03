import random as r
difficulty=int(input("Enter your difficulty (1-3)\n"))
if difficulty==3:
    highest_num=1000
elif difficulty==2:
    highest_num=500
elif difficulty==1:
    highest_num=100
answer=r.randint(1,highest_num)
exp_counter=1
tries=0
while exp_counter<highest_num:
    exp_counter*=2
    tries+=1
handicap=3-difficulty
tries+=handicap
print(f'I have picked a number from 1 to {highest_num}. After each guess I will tell you if your guess wwas too low or too high.')
while tries>0:
    guess=int(input("Enter your guess:\n"))
    tries-=1
    if guess==answer:
        print("You won!")
        exit()
    elif guess<answer: print("Your guess was too low")
    elif guess>answer: print("Your guess was too high")
    print(f'You have {tries} guesses left')