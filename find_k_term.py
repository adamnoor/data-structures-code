def find_k(list, target):
    
    middle = len(list)//2
    frequency = 1
    if list[middle] == target:
        l = middle + 1
        r = middle -1
        for i in range (l, len(list)):
            if list[i] == target:
                frequency += 1
            else:
                break
        for i in range (r, 0, -1):
            if list[i] == target:
                frequency += 1
            else:
                break
        print([target, frequency])
        return 1
    
    if list[middle] > target:
        left = list[:middle]
        if len(left) > 1:
            find_k(left, target)
        else:
            if left[0] == target:
                print([target, 1])
            else:
                print ("Target is not in the list")
    elif list[middle] < target:
        right = list[middle:]
        if len(right) > 1:
            find_k(right, target)
        else:
            if right[0] == target:
                print([target, 1])
            else:
                print ("Target is not in the list")

find_k(list = [1, 2, 2, 2, 2, 7], target = 3)
find_k(list = [1, 2, 2, 3, 2, 2, 7], target = 3)
find_k(list = [1, 2, 2, 2, 2, 3, 7], target = 3)
find_k(list = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], target = 3)
find_k(list = [3, 3, 3, 3, 3, 3, 3, 3, 3], target = 3)
find_k(list = [3, 4, 5], target = 3)
