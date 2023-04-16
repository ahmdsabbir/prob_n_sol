'''
Given an integer n, print all integers from 1 to n
but print fizz when integer is divided by 3 
and print buzz when divided by 5
'''

n = 66

for i in range(1, n):
    if i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
