class Solution:
    def intToRoman(self, num: int) -> str:
        rmn = ""
        current = num
        roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        
        for i in range(1, current//1000 + 1):
            rmn = rmn + "M"
        current = current % 1000
        
        while current >= 400:
            if current >= 900:
                rmn = rmn + "CM"
                current = current % 900
            elif current < 900 and current >=500:
                for i in range(1, current // 500 + 1):
                    rmn = rmn + "D"
                current = current % 500
            else:
                rmn = rmn + "CD"
                current = current % 400
        
        for i in range(1, current//100 + 1):
            rmn = rmn + "M"
        current = current % 100
        
        
        while current >= 40:
            if current >= 90:
                rmn = rmn + "XC"
                current = current % 90
            elif current < 90 and current >=50:
                for i in range(1, current // 50 + 1):
                    rmn = rmn + "L"
                current = current % 50
            else:
                rmn = rmn + "XL"
                current = current % 40
        
        for i in range(1, current//10 + 1):
            rmn = rmn + "M"
        current = current % 10
        
        
        while current >= 4:
            if current >= 9:
                rmn = rmn + "IX"
                current = current % 9
            elif current < 9 and current >=5:
                for i in range(1, current // 5 + 1):
                    rmn = rmn + "V"
                current = current % 5
            else:
                rmn = rmn + "IV"
                current = current % 4
        
        for i in range(1, current + 1):
            rmn = rmn + "I"
        
        return (rmn)

    
solution = Solution()
print(solution.intToRoman(1994))
