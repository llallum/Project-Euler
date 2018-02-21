"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

lmc =2
>>> for i in range(2,21):
        lcm = lcm*i/gcd(lcm,i)