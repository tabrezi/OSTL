#This is single line comment. First program in Python
#Experiment 1, Program 1.1
#Program to implement Comments, Datatypes, Expressions, Input and Output Functions
'''
Multiline comment as a multiline constant string using 
triple quotes which should be used only for learning purpose 
otherwise it is not recommended while developing any application software.
'''
#Illustrating datatypes
'''
theory can be put here
'''
print('Illustrating Datatypes')
i=10
f=20.5
s='Hello World'
c=2+3j                  #complex number
print('Integer value:', i, '\nFloat value:', f,'\nString:', s,'\nComplex number:',c)
print('Type of', i, 'is',type(i),'\nType of', f,'is',type(f),'\nType of', s,'is',type(s),'\nType of',c,'is',type(c))

#Illustrating Expressions
print('Illustrating Expressions')
print('Division is',21/i)
print('Quotient is',21//i)
print('Remainder is',21%i)
print('Power of 2 to 3 is',2**3)   #can also be written as pow(2,3)
x,y=divmod(5,2)
print('Divmod of 5/2 is ',x,y)
#print("Divmod of 5/2 is",divmod(5,2))

#Illustrating Input Output functions
print('Illustrating Input Output functions')
i=int(input('Enter Integer number: '))
f=float(input('Enter Floating number: '))
s=input('Enter String: ')
c=complex(input('Enter Complex number: '))
print('Integer value:', i, '\nFloat value:', f,'\nString:', s,'\nComplex number:',c)
