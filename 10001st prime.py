"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import math

def prime(var):
        if var == 2 or var == 3:
                return True
        i = 2

        while (i < math.sqrt(var)+1):
                if var%i == 0:
                        return False
                i+=1
        
        return True

i=2
counter = 0
while counter <10001:
        if prime(i) == True:
                counter+=1
                
        i+=1

i-=1
print i