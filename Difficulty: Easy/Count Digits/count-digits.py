#User function Template for python3


# class Solution:
#     def evenlyDivides (self, N):
#         # code here
#         counter = 0
        
#         for i in str(N):
#             if int(i) != 0 and N%int(i) == 0:
#                 counter+=1
        
#         return counter

class Solution:
    def evenlyDivides (self, N):
        counter, n = 0, N
        while(N>0):
            digit = N % 10
            if digit != 0 and n%digit == 0:
                counter+=1
            N = N//10 
            
        return counter
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends