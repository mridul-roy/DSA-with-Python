#Count length
n = 67896789506695874637
num = n
count = 0
while num>0:
    last_num = num%10
    # print(last_num);
    num = num // 10
    count = count+1
print(count)

#Time Complexity - O(log10(N))
    
#Check Palindrome Number

n = 66666

num = n
result = 0
while num>0:
    last_digit = num%10
    result = (result*10)+last_digit
    num= num//10


if n == result:
    print(f"{result} is Palindrome Number")
else:
    print(f"{result} is not Palindrome Number")
    

#Time Complexity - O(log10(N))

# Armstrong Number

n = 153
num = n
total = 0
nod = len(str(num))
while num>0:
    last_digit = num%10
    total = total+(last_digit**nod)
    num = num//10
    
if n == total:
    print(f"The {total} is Armstrong Number")
    
else:
    print(f"The {total} is not Armstrong Number")
    
#Time complexity O(log10)^N

#Print all Factors

n = 10
num = n
result = []
for i in range(1,num):
    if num%i == 0:
        result.append(i)

print(result)

#Time complexity O(N)


def finds_factor(n):
    num = n
    result = []
    for i in range(1,(num//2)+1):
        if num%i == 0:
            result.append(i)
    return result

print(finds_factor(20))

#Time complexity O(N) 



from math import sqrt

n = 36
num = n
result = []
for i in range(1,int(sqrt(n))+1):
     if num%i == 0:
        result.append(i)
        if num//i != i:
            result.append(num//i)
            result.sort()
print(result)

#Frequency map in Dictionary

nums = [2,4,3,54,54,64,3,7,75,43,5,2,3,1,7]
freq_map = {}
x = 5
for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]] = 1
print(freq_map)
print(freq_map[x])

#Time complexity O(N)
#Space Complexity O(1)


nums = [2,4,67,3,6,32,65,2,4,3,1,7,8,22]
n = len(nums)
hash_map = {}
for i in range(0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
    
print(hash_map)


#Time complexity O(N) 