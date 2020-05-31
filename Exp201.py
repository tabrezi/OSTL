#Experiment 2, Program 2.1
#program to implement the Control Structures
#if elif else
'''
Theory about control structures in Python
'''
num1=int(input('Enter number: '))
num2=int(input('Enter number: '))
num3=int(input('Enter number: '))

if(num1 > num2):
    if num1 > num3:
        print(num1, 'is largest.')
    else:
        print(num3, 'is largest.')
elif(num2 > num3):
    print(num2, 'is largest.')
else:
    print(num3, 'is largest.')
s1=input('Enter String: ')
s2=input('Enter String: ')
if s1.upper() == s2.upper():
    print('Similar')
else:
    print('Not Similar')
print(id(s1))
s1+=' says Hello to ' + s2  # s1 = s1 + " say hello to " + s2
print(s1)
print(id(s1))
s2=s1
print(id(s2))

s3='Computer says Hello to World'
print(id(s3))
s4='Computer says Hello to World'
print(id(s4))

