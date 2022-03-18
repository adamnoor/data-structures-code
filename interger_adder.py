
# Online Python - IDE, Editor, Compiler, Interpreter

import time

def integerAdder(list):
    tic = time.perf_counter()
    count = 0
    term = 0
    for element in reversed(list):
        number = int(element) * (10 ** count)
        term += number
        count += 1
    term += 1
    list.clear()
    for char in str(term):
        list.append(int(char))
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.7f} seconds")
    print(list)

#def betterAnswer(A: List[int]) -> List[int]: #What is this and why doesn't it work
def betterAnswer(A):
    tic = time.perf_counter()
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    else: #why does the indentation align with the for loop and not the if statement?
        if A[0] == 10:
            A[0] = 1
            A.append(0)
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.7f} seconds")
    print (A)
    
    

betterAnswer([1])
betterAnswer([1, 0, 9])
betterAnswer([1, 2, 9])
betterAnswer([9,9,9])
betterAnswer([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9])
integerAdder([1])
integerAdder([1, 0, 9])
integerAdder([1, 2, 9])
integerAdder([9,9,9])
integerAdder([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9])
