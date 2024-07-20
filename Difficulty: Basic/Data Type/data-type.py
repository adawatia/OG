#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def dataTypeSize(self, str):
        # Code here
        dic = {
        "character" : 1,
        "integer" : 4,
        "short" : 2,
        "long" : 8,
        "float" : 4,
        "double": 8}
        str = str.lower()
        if str in dic.keys():
            return dic[str]
        else:
            return -1
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
# } Driver Code Ends