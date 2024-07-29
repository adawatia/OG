def brute(a:int,b:int)->int: 
    gcd =1
    for i in range(1,min(a,b)+1):
        if(a%i == 0 and b%i == 0):
            gcd = i
            
    return gcd
    
def better(a:int,b:int)->int: 
    for i in range(min(a,b),0,-1):
        if(a%i == 0 and b%i == 0):
            return i
            
    return 1

def optimal(a:int,b:int)->int: #Euclidean Algorithm 
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b%a
        
    if a == 0:
        return b
    
    return a


def main():
    n = int(input())
    while(n):
        a, b = map(int, input().split())
        print(optimal(a,b))
        n-=1
    
if __name__ == "__main__":
    main() 