#Experiment 2, Program 2.2
#program to implement the For Loop
#for loop
'''
Theory about it
'''
n=int(input('Enter the number: '))
f=1
for i in range(1,n+1):
    f=f*i
print('Factorial of',n,'is',f)

a,b=0,1
c=a+b
print('Fibonacci Series till',n,':',a,b,end=' ')
#while loop
'''
theory about it
'''
while c<=n:
    print(c,end=' ')
    a,b=b,c
    c=a+b
print('')