
def loop(n:int)->int:
    fact = 1
    for i in range(1,n+1):
        fact = i * fact
        
    return fact


def factorial(n:int)->int:
    if n == 0:
        return 1
    return n*factorial(n-1)

def main():
    print(loop(3))
    print(factorial(3))
    
if __name__ == "__main__":
    main()