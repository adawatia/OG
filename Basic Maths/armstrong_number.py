def isArmstrong(num):
    # Write your code here.
    k = len(str(num))
    dup = num
    total = 0
    while(num > 0):
        digit = num %10
        total += pow(digit,k)
        num //= 10
    
    return True if dup == total else  False

