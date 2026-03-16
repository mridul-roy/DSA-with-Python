nums = [34,63,5,-4,56,24,5,336]

# def func():
#     largest = nums[0]
#     n=len(nums)
#     for i in range(0,n):
#         largest=max(largest,nums[i])
#     return largest

# print(func()) 


def func():
    largest = float("-inf")
    n=len(nums)
    for i in range(0,n):
        largest=max(largest,nums[i])
    return largest

print(func())