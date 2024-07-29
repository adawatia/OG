def brute_method(N:str) -> bool:
    print(N[::-1])
    
    
def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]
        if rev == str(x):
            return True
        else:
            return False

def checkPalindrome(s):
    # Write your code here
	# Return a boolean
	filtered_str  = ""

	for i in s:
		if i.isalnum():
			filtered_str += i

	return True if filtered_str.lower() == filtered_str[::-1].lower() else False


def main():
    # input_1 = input("Enter a string: ")
    brute_method("Devansh")
    pass

if  __name__ == "__main__":
    main()