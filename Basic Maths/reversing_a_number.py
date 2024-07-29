def reverse(N:int)-> None:
    reverse_number = 0
    while(N>0):
        digit = N % 10
        reverse_number = (reverse_number*10) + digit 
        N //=10
        
    print(reverse_number)
    
        

def main():
    number = int(input("Enter value: "))
    reverse(number)
    
if __name__ == "__main__":
    main() 