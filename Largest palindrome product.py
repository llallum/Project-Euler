"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""




def factorial(var, digits):
        counter = 10 ** (digits-1)
        upper_limit = 10 **(digits)
        lower_limit = counter
        
        while var/counter > 2:
                if var%counter == 0:
                        if (counter > lower_limit and counter < upper_limit)  and (var/counter < upper_limit and var/counter > lower_limit):
                                print "multiplicand :" , counter
                                print "multiplier   :", var/counter
                                return True
                counter += 1
        return False
                                

def checkPalindrome(originalInteger):

        n = originalInteger
        new = 0
        list1 = []
        counter = 0

        while (n/10 > 0):
                r = n%10
                n = n/10
                list1.append(r)  

        list1.append(n)

        counter = len(list1)
        counter_2 = 0

        while counter > 0:     
                new += list1[counter-1] * (10**counter_2)
                counter-=1
                counter_2+=1

        if originalInteger == new:
                return True
        else:
                return False


""" The largest number of 3 digits product 999*999 """


upper_limit = input("Input upper limit for palindrome (100, 1000, 10000 ....etc) : ")
lower_limit = input("Input lower limit for palindrome (10, 100, 1000....etc) : ")
number_of_digits = input("Input number of digits: ")


while upper_limit > lower_limit:
        if checkPalindrome(upper_limit) == True:
                if factorial(upper_limit,number_of_digits) == True:
                        print "found :", + upper_limit
                        break
                print upper_limit
        upper_limit-=1


