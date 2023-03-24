while True:
    n = int(input("Enter a number 0 to exit: "))
    if n > 0:
        print("We only allow negative number. Please try again.")
        continue
    if n == 0:
        break 
    print("Square of", n, "is", n*n)
    
    
    