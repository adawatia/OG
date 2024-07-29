def print_1_to_N_using_recursion(i:int,n:int):
    if(i >n):return
    print(i)
    print_1_to_N_using_recursion(i+1,n) 
    pass

def main():
    print_1_to_N_using_recursion(1,10)
    
if __name__ == "__main__":
    main()