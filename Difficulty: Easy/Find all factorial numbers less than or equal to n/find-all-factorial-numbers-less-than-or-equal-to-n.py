#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	#code here
    	res = []
        fact = 1
        i = 1
        while fact <= n:
            res.append(fact)
            i += 1
            fact *= i
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends