##______Reverse Array with Recursive Function_______##

nums = [3, 4, 6, 1, 5, 8, 9, 7]

def func(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    
    func(arr, left + 1, right - 1)

def reverse_array(nums,l=0,r=len(nums) - 1):
    func(nums, l, r)
    return nums  

result = reverse_array(nums)
print(result)


# Check string is palindrome or not

S = "nitin"

def func(S, left, right):
    if left >= right:
        return True
    if S[left] != S[right]:
        return False
    return func(S,left+1, right-1)

print(func(S,0, len(S)-1))


## Fibonacci Number with loop and Recursion


def func(num):
    if num == 0 or num == 1:
        return num
    return func(num-1)+func(num-2)

print(func(7))

## Time complexity O(N^2)