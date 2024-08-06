def is_palindrome(s:str)->bool:
    left = 0
    right = len(s)-1
    while(left < right):
        if not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right-=1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left +=1
            right -=1
    
    return True

def main():
    print(is_palindrome("A man, a plan, a canal: Panama"))
    pass
if __name__ == '__main__':
    main()