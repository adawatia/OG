def print_N_to_1_using_recursion(i:int,n:int):
    if(i < n):return
    print(i)
    print_N_to_1_using_recursion(i-1,n) 
    pass

def main():
    print_N_to_1_using_recursion(10,1)
    
if __name__ == "__main__":
    main()