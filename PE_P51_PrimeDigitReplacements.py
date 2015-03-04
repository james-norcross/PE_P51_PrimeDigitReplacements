## Author: James Norcross
## Date: 3/2/15
## Description: Finds the smallest prime that is a member of an eight member
## prime family

from math import sqrt
from math import log10

## a prime sieve function
def makePrimeSieve(max):
    sieve = []
    
    ## initialize to true
    for i in range(max):
        sieve.append(True)
        
    ## make sieve
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True
    
    imax = int(sqrt(max)) + 1
    
    for i in range(2,imax):
        if(sieve[i]):
            for j in range(2*i, max, i):
                sieve[j] = False

    return sieve

## creates a list from sieve
def listFromSieve(sieve):
    
    myList = []
    
    for i in range(0, len(sieve)):
        if (sieve[i]):
            myList.append(i)

    return myList

## determines whether a number is an appropriate mask for creating a
## prime family.  Such a mask must contain only zeroes and one other digit (which
## may occur numerous times). 1 is not a valid mask and neither is all 1's.
## number is integer, returns -1 if number is not
## a valid mask, otherwise returns the reduced mask represented by number 
def findMask(n1, n2):

    original = n1
    diff = n1-n2
    maskDigit = 0
    n1Digit = 0
    
    while(diff > 0):
        digitn1 = n1 % 10
        digit = diff % 10
        if(digit != 0):
            if(maskDigit == 0):
                maskDigit = digit
                n1Digit = digitn1
                if(n1Digit < 7):        ## limit for family containing 8 members
                    return -1
            elif(digit == maskDigit):
                if(digitn1 != n1Digit):
                    return -1
            else:
                return -1

        diff = diff / 10
        n1 = n1/10

    reducedMask = (original-n2)/maskDigit
    
    if(reducedMask == 1):
        return -1

    if(list(str(reducedMask)).count('0') == 0):
        return -1
    
    return reducedMask

## generates a family of primes given a starting prime, mask and prime sieve
## number, mask ints and sieve a boolean list
## returns a list of the prime family
def generateFamily(number, mask, sieve):

    ## calculate termination for family generating loop
    orderNumber = int(log10(number))
    orderMask = int(log10(mask))
    if(orderNumber > orderMask):
        terminate = number - (number % (10**(orderMask+1)))
    else:
        terminate = 10**orderMask

    ##generate family
    family = []
    while(True):
        if(number < terminate):
            break
        else:
            if(sieve[number]):
                family.append(number)
            number -= mask

        
    return family

    
                
            

maxNumber = 1000000

## initialize prime sieve and list
isPrime = makePrimeSieve(maxNumber)
primes = listFromSieve(isPrime)

##n1 = 56993
##n2 = 56773
##a = findMask(n1,n2)
##print a
##print generateFamily(n1, a, isPrime)
for i in range(-1,-len(primes)-1, -1):
    for j in range(i-1, -len(primes) - 1, -1):
        
        a = findMask(primes[i], primes[j])
        if(a != -1):
            family = generateFamily(primes[i], a, isPrime)
            if(len(family) > 6):
                print family
