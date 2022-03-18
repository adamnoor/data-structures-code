# Online Python - IDE, Editor, Compiler, Interpreter
import random

def generateArray():
    arr = [random.randint(1,10) for _ in range(1000)]
    return arr

def stockFinder(list):
    max = 0
    buy = 0 
    sell = 0
    count = 0
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            count += 1
            if(list[j] - list[i] > max):
                max = list[j] - list[i]
                buy = list[i]
                sell = list[j]
                
            
    
    print("Max profit is " + str(max))
    print("Buy price is " + str(buy))
    print("Sell price is " + str(sell))
    print("Number of days is " + str(len(list)))
    print("Count is " + str(count))
    print(count/len(list))

stockFinder(generateArray())
# stockFinder([310, 315, 275])
# stockFinder([310, 315, 275,310, 315, 275]) 
# stockFinder([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
# stockFinder([310, 315, 275, 295, 260, 270, 290, 230, 255, 450, 220, 230, 400, 410, 0, 100, 200, 310, 315, 275, 295, 260, 270, 290, 230, 255, 450, 220, 230, 400, 410, 0, 100, 200])

    
