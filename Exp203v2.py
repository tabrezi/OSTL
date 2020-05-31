#Experiment 2, Program 2.3
#program to implement the functions
'''
theory about functions in python
'''
def fact(n):
    """Function to return factorial of given number"""
    if(type(n)==int):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
    else:
        return 'Cannot find the factorial of non-integer value.'

def fibo(n):
    '''
    Its a fibonacci function which returns a list containing fibonacci series till given number.
    It accepts an integer value.
    '''
    l=list()
    l.append(0)
    l.append(1)
    while l[-1]+l[-2] <=n:
        l.append(l[-1]+l[-2])
    return l

def chkprime(n):
    ''' Function to check the primality of given number.'''
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True

def sumfibo(n):
    l=fibo(n)
    sum=0
    for i in l:
        sum+=i
    return sum
if(__name__=='__main__'):
    n=int(input('Enter the number: '))
    while True:
        print('\t\t\tMENU\n1. Factorial.\n2. Fibonacci.\n3. Summation of Fibonacci.')
        print('4. Primality.\n5. Exit.')
        ch=int(input('Enter your Choice::'))
        if(ch==1):
            print('Factorial of',n,'is',fact(n))
        elif(ch==2):
            print('Fibonacci Series till',n,'is',fibo(n))
        elif(ch==3):
            print('Summation of Fibonacci Series till',n,'is',sumfibo(n))
        elif(ch==4):
            print('Primality of ',n,' is ',chkprime(n))
        elif(ch==5):
            break
        else:
            print('Please enter correct choice...')
    #print(fact.__doc__)
