# Online Python - IDE, Editor, Compiler, Interpreter

import random

def generateArray():
    arr = [random.randint(1,10) for _ in range(100000)]
    return arr

def stock_finder_fast(list):
    
    max_profit = 0
    min_price_so_far = list[0]
    count = 0
    for price in list:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
        print("min price so far:" + str(min_price_so_far))
        print("max profit sell today:" + str(max_profit_sell_today))
        print("max profit:" + str(max_profit))
        print("the count is:" + str(count))
        print("")
        count += 1
    
    return max_profit


print(stock_finder_fast([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
#print(stock_finder_fast(generateArray()))

