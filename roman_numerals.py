class Solution:
    def intToRoman(self, num: int) -> str:
        rmn = ""
        
        for i in range(1, num//1000 + 1):
            rmn = rmn + "M"
        num = num % 1000
        
        while num >= 400:
            if num >= 900:
                rmn = rmn + "CM"
                num = num % 900
            elif num < 900 and num >=500:
                for i in range(1, num // 500 + 1):
                    rmn = rmn + "D"
                num = num % 500
            else:
                rmn = rmn + "CD"
                num = num % 400
        
        for i in range(1, num//100 + 1):
            rmn = rmn + "C"
        num = num % 100
        
        
        while num >= 40:
            if num >= 90:
                rmn = rmn + "XC"
                num = num % 90
            elif num < 90 and num >=50:
                for i in range(1, num // 50 + 1):
                    rmn = rmn + "L"
                num = num % 50
            else:
                rmn = rmn + "XL"
                num = num % 40
        
        for i in range(1, num//10 + 1):
            rmn = rmn + "X"
        num = num % 10
        
        
        while num >= 4:
            if num >= 9:
                rmn = rmn + "IX"
                num = num % 9
            elif num < 9 and num >=5:
                for i in range(1, num // 5 + 1):
                    rmn = rmn + "V"
                num = num % 5
            else:
                rmn = rmn + "IV"
                num = num % 4
        
        for i in range(1, num + 1):
            rmn = rmn + "I"
        
        return (rmn)

    
solution = Solution()
print(solution.intToRoman(1994))
