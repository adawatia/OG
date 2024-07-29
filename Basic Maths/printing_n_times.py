def n_times(n:int):
    if (n<1):return
    n_times(n-1)
    print(n,end=" ")
    pass

def main():
    n_times(10)
    
if __name__ == "__main__":
    main()