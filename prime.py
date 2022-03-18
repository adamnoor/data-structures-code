
# Online Python - IDE, Editor, Compiler, Interpreter


def prime(nbr):
    list = []
    start = 1
    if(nbr < 3):
        list = []
    elif(nbr == 3):
        list.append(2)
    else:
        list.append(2)
        list.append(3)
    
    while start * 6 - 1 < nbr:
        list.append(start * 6 - 1)
        if(start * 6 + 1 < nbr):
            list.append(start * 6 + 1)
        start += 1
    
    if(len(list) < 100):
        print(list)
    else:
        print("List for " +  str(nbr) + " is too long to print")
    print("The number of prime numbers is " + str(len(list)))

prime(0)
prime(9)
prime(2)
prime(3)
prime(-2)
prime(100000)
prime(18)
