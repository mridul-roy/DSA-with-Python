nums = [45,32,775,-334,7,22,668]

# def func():
#     largest = float("-inf")
#     s_largest = float("-inf")
#     n = len(nums)
#     for i in range(0,n):
#         largest=max(largest,nums[i])
#     for i in range(0,n):
#         if nums[i]>s_largest and nums[i]!=largest:
#             s_largest = nums[i]
#     return s_largest

# print(func())

## Time complexity -> O(N)
## Space complexity -> O(1)


def func():
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)
    for i in range(0,n):
        if nums[i]>largest:
            s_largest=largest
            largest=nums[i]
        elif nums[i]>s_largest and nums[i]!=largest:
            s_largest=nums[i]
    return s_largest

print(func())        
    