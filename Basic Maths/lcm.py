def optimal(a:int,b:int)->list: #Euclidean Algorithm 
    res  = []
    A,B = a,b
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b%a
            
    if a == 0:
        res.append(b)
    else:
        res.append(a)
    
    lcm = (A*B)//res[0]
    res.append(lcm)
    return res

def main():
    n = int(input())
    while(n):
        a, b = map(int, input().split())
        print(optimal(a,b))
        n-=1
    
if __name__ == "__main__":
    main() 