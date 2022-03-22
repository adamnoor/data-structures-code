arr1 = [1, 2, 3, 2, 1]
is_palindrome = True
count = 0

for i in range(0, len(arr1)//2):
    if(arr1[i] != arr1[~i]):
        is_palindrome = False
        break
    count+=1


print(is_palindrome)
print(count)
