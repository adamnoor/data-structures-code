# Online Python - IDE, Editor, Compiler, Interpreter

def product(arr1, arr2):
    result = []
    def integerize(list):
        neg = False
        number = 0
        exp = 0
        if(list[0] == "-"):
            neg = True
            list.remove(list[0])
        for element in reversed(list):
            number += element * 10 ** exp
            exp += 1
        if(neg):
            number = number * -1
        return number
    
    product = str(integerize(arr1) * integerize(arr2))
    for dig in product:
        result.append(dig)
    
    print(result)
        
        

product(["-", 2, 3, 4, 5], ["-", 1])
product(["-", 2, 3, 4, 5], ["-", 2])
product(["-", 2, 3, 4, 5], ["-", 2, 3, 4, 5])
product(["-", 2, 3, 4, 5], [2, 3, 4, 5])
product(["-", 2, 3, 4, 5], [0])
