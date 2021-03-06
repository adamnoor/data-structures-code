# Online Python - IDE, Editor, Compiler, Interpreter

import random

def generateArray():
    arr = [random.randint(1,10) for _ in range(10000)]
    return arr

def rearrange_list(list):
    i = 0 #current position
    min_position = 0
    min_value = list[0]
    max_value = list[1]
    for i in range(0, len(list)):
        if (i%2 != 0):
            #look for min since the current position for comparison starts in an odd index
            for j in range(i+1, len(list)):
                if(list[i] < list[j]):
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
                
        else:
            for j in range(i+1, len(list)):
                if(list[i] > list[j]):
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
         
    return (list)


print(rearrange_list([1, 2, 3]))
print(rearrange_list(generateArray()))
