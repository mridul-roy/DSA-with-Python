nums = [3,4,1,9,5,7,1]

def func(nums):
    n = len(nums)
    for i in range(0,n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1]=key
    return nums
        
print(func(nums))