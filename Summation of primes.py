"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

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

i = 2
sum_of_primes = 0
while i<2000000:
        if prime(i) == True:
                sum_of_primes+=i
        i+=1

print sum_of_primes