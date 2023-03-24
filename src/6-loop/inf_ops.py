terminate_program = False

while not terminate_program:
    n1 = int(input('Enter a number: '))
    n2 = int(input('Enter another number: '))
    
    while True:
        ops = input("enter add/sub or quit to exit: ")
        if ops == "quit":
            terminate_program = True 
            break 
        if ops not in ["add", "sub"]:
            print("Unknown ops")
            continue 
        if ops == "add":
            print("Result is : ", n1 + n2)
            break
        if ops == "sub":
            print("Result is : ", n1 - n2)
            break 
        