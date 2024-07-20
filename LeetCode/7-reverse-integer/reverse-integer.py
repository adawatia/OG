class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        reverse_number = 0
        neg = x < 0
        
        if neg:
            x = -x
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow/underflow
            if (reverse_number > INT_MAX // 10) or (reverse_number == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            
            reverse_number = reverse_number * 10 + digit
        
        return -reverse_number if neg else reverse_number