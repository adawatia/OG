#User function Template for python3

class Solution:
    def lcmAndGcd(self, a , b):
        res = []
        A, B = a, b
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
                
        if a == 0:
            gcd = b
        else:
            gcd = a
        
        lcm = (A * B) // gcd
        
        res.append(lcm)  # Append LCM first
        res.append(gcd)  # Append GCD second
        
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends