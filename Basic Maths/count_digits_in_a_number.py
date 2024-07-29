Problem =   """
Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.
Example 2:
Input:N = 7789
Output: 4
Explanation: The number 7789 has 4 digits.

    """

Problem_2 = """
Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

"""
# Simple Method using inbuilt function
def digits(N:int) -> int:
    return len(str(N))

# Brute Force Method

def brute(N: int) -> int:
    counter = 0
    
    while(N>0):
        counter += 1
        N//= 10
    return counter

import math
def log_method(N: int)-> int:
    return int(math.log10(N)+1)

def divisible_digits(N: int) -> int:
    counter, n = 0, N
    while(N>0):
        digit = N % 10
        if digit != 0 and n%digit == 0:
            counter+=1
        N = N//10 
        
    return counter
    pass

def main():
    number = int(input("Enter value: "))
    # print(digits(number))
    # print(brute(number))
    print(divisible_digits(number))
    
if __name__ == "__main__":
    main() 