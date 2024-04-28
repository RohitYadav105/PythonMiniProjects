print("choose the order:\n (1) : increasing \n (2) : decresing")
order = int(input("press: "))
if order == 1:
    print("enter your choice:\n (1) : rowise \n (2) : column")
    choice = int(input("press: "))
    
    if choice == 1:
        start = int(input("enter the starting point: "))
        end = int(input("enter the ending point: "))
        update = int(input("enter the update point: "))
        for i in range(start, end + 1, update):
            print(i, end=" ")
            
    elif choice == 2:
        start = int(input("enter the starting point: "))
        end = int(input("enter the ending point: "))
        update = int(input("enter the update point: "))
        for i in range(start, end + 1, update):
            print(i)
    else:
        print("not a valid input")

elif order == 2:
    print("enter your choice:\n (1) : rowise \n (2) : column")
    choice = int(input("press: "))
    
    if choice == 1:
        start = int(input("enter the starting point: "))
        end = int(input("enter the ending point: "))
        update = int(input("enter the update point: "))
        numbers = list(range(start, end - 1, -update))      
        for i in numbers:
            print(i, end=" ")
            
    elif choice == 2:
        start = int(input("enter the starting point: "))
        end = int(input("enter the ending point: "))
        update = int(input("enter the update point: "))
        numbers = list(range(start, end - 1, -update))
        
        
        for i in numbers:
            print(i)
            
    else:
        print("not a valid input")
else:
    print("syntax error")