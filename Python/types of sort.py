import random as r


def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def flag_bubble(arr):
    for i in range(len(arr) - 1):
        flag = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if flag == False:
            break
    return arr

def shaker(arr):
    left = 0
    right = len(arr) - 1
    while left<right:
        r_new = left
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                r_new = i
        right = r_new
        l_new = right
        for i in range(right - 1, left - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                l_new = i
        left = l_new
    return arr


def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q =  (nums[0]+nums[len(nums)-1])//2
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)


def vibor(arr):
    if len(arr) <= 1:
        return arr
    else:
        for i in range(len(arr)):
            lowest = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[lowest]:
                    lowest = j
            arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


def vstavki(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur
    return arr


print([5,2,65,1,4,2,66,2,5].sort())

