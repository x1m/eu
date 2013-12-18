__author__ = 'x1m'

def prime(num):
    ''' is the number Primer, True or False '''
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True
#good for nothing - rewrite
#--------------------

def isPal(pal):
    pal_2 = pal[::-1]
    if pal == pal_2:
        print(pal)
        #return True
   # return False
#--------------------



li = [(x, y)
    for x in range(13)
    for y in range(13)
    if x + y == 12
    if x >= y]
    print(li)