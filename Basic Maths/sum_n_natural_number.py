def sum_using_loop(n:int)->int:
    total = 0
    for i in range(1,n+1):
        total += i
    
    return total

def using_formula(n:int)->int:
    return n*(n+1)//2

def using_recursion(i,sum:int)->int:
    if(i < 1):
        return sum
    return using_recursion(i-1,sum+i)

def using_recursion_2(sum:int)->int:
    if sum ==0:
        return 0
    return sum+using_recursion_2(sum-1)

def main():
    print(sum_using_loop(3))
    print(using_formula(3))
    print(using_recursion(3))
    print(using_recursion_2(3))
    
    pass

if __name__ == "__main__":
    main()