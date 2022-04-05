q_grades=[4,4,4,4]
final=4
total=0
for grade in q_grades:
    total+=(grade*0.225)
total+=(final*0.1)
#A A A A 
print(total)
final=4
while final>=0:
    q_sum=16
    while q_sum>0:
        total=(q_sum*0.225)+(final*0.1)
        if 3>total>2.5:
            print(f'quarter total of {q_sum} and final of {final} will give a {total} score')
        q_sum-=1
    final-=1

#A=4
#B=3
#C=2
#D=1

#Q1:A, Q2:B, Q3:A, Q4:D
#quarter total=4+3+4+1=10

#For Overall A (3.5-4.0):
#Cannot get A with a quarter total of 13
# quarter total of 14 and final of 4 will give a 3.55 score
# quarter total of 15 and final of 2 will give a 3.575 score
# quarter total of 16 and final of 0 will give a 3.6 score

#For Overall B (2.5-3.49):
#Cannot get B with a quarter total of 9
# quarter total of 10 and final of 3 will give a 2.55 score
# quarter total of 11 and final of 1 will give a 2.575 score
# quarter total of 12 and final of 0 will give a 2.7 score