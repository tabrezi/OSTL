#Experiment 1, Program 1.2
#Program to implement Byte Array, Range, Set and String Functions
#Bytearrays
'''
Theory about Bytearrays
'''
b=bytearray(3)
print(b[0], b[1], b[2])
c=b'HEllo'
print(c)
print(type(c))

#Range
print('\nIllustrating Range:')
r=range(5)
print(r[0],r[4])
r=list(range(10,20))
print(r)

#Set
print('\nIllustrating Set')
s1={1,2,3}
print('Set-1:',s1)
s2={3,4,5,6}
print('Set-2:',s2)
print('Union:',s1.union(s2))
print('Intersection:',s1.intersection(s2))
print('Is',s1.union(s2),'superset of',s1,'?',s1.union(s2).issuperset(s1))
#print(type(s1))

#String functions
print('\nIllustrating String functions:')
s=input('Enter String: ')
subs=input('Enter Substring: ')
print('Reverse String is',s[::-1])  #using slicing with -1 as step value
print('Is',subs,'substring of',s,'?',subs in s)
print('Uppercased:',s.upper())