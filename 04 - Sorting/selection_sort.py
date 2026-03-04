## Selection sort 

# nums = [6,2,5,7,1,6,25,3,1]

# def selection_sort(nums):
#     n = len(nums)
#     for i in range(0,n):
#         min_index = i
#         for j in range(i+1,n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     return nums
                
    
    
# print(selection_sort(nums))


nums = [2,700,890,45,88,65,7,4,3,3,1]

def selection_sort(nums):
    n = len(nums)
    for i in range(0,n):
        max_index = i
        for j in range(i+1,n):
            if nums[max_index] < nums[j]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return nums


print(selection_sort(nums))
