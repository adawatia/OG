def name_n_times(i:int,n:int):
    if(i > n):return
    print("Devansh "+str(i))
    name_n_times(i+1,n)
    pass

def main():
    name_n_times(1,10)
    
if __name__ == "__main__":
    main()