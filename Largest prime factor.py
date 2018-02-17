"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


def prime(var):
        if var == 2 or var == 3:
                return True
        i = 2

        while i < var/2:
                if var%i == 0:
                        return False
                i+=1
                
        return True

def factorial_1(var):
        if prime(var) == True:
                print var
                return

        counter = 2
        while var/2 > 2:    
                if var%counter == 0:
                        if prime(counter) == True:
                                factorial_1(var/counter)
                                return
                        else:
                                factorial_1(counter)
                counter += 1

var1 = 600851475143  

factorial_1(var1)