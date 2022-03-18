
# Online Python - IDE, Editor, Compiler, Interpreter

def deleteItem(list):
    i = 0
    while i < len(list) - 1:
        if(list[i] == list[i+1]):
            list.pop(i+1)
        else:
            i += 1
        
    print (list)
    print(len(list))

deleteItem([0, 0, 1, 1, 2, 2, 3, 4, 4])
deleteItem([])
deleteItem([1, 1, 1, 1])
deleteItem([1, 2, 3, 4])
