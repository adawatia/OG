#User function Template for python3

class Solution:
    def sumOfDivisors(self, n):
        # code here 
        if n ==0:
            return 0
        
        div_total = 0
        
        for i in range(1, n + 1):
            div_total += (i * (n // i))
        
        return div_total

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends