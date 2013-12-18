__author__ = 'x1m'

##  1
def first():
    r = 0
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            r += i
    print(r)

#first()
#--------------------

##  2 (fib)
def second(max):
    a, b = 0, 1
    r = 0
    while a < max:
        a, b = b, a + b
        #print(a, end=' ')
        if a % 2 == 0:
            r += a
    print(r)

#second(4000000)
#--------------------


def third(num):    #Prime numbers
    i = 2
    while i*i < num:
        while num % i == 0:
            num = num / i
        i = i + 1
    print(num)

#third(600851475143)
#--------------------

def forth(): #Palindromes

    n = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            x = i * j
            if x > n:
                s = str(x) #(i * j)
                if s == s[::-1]:
                    n = i * j
    print(n)
    #even if the palindrome is found the cycles continue
    #and that is bad
#forth()
#--------------------

#def fifth():

request = input('enter your request: ')

#fifth()












