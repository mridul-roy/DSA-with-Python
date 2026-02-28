######___________Hash Map and Dictionary___________######
# #Constrains
#     1. 1<=n[i]<=10
#     2. n can be 10^8
#     3. m can be 10^8

n = [2,4,5,6,3,54,8,5,7,9,4,2]
m = [2,5,3,5,6,73,45,3,5,3,15]

for i in m:
    count = 0
    for x in n:
         if x == i:
             count+=1
    print(count) 

#Time Complexity -> O(N*M)

#Alternative

n = [2,4,5,6,3,5,8,5,7,9,4,2]
m = [2,7,4,5,3,100]

hash_list = [0]*11
for num in n:
    hash_list[num]+=1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])
        
# Time Complexity -> O(N+M)
# Space Complexity -> O(11) -> O(1)


n = [2,4,5,6,3,5,8,5,7,9,4,2]
m = [2,7,4,5,3,100]

hash_dict = {}
for i in range(0,len(n)):
    hash_dict[n[i]]= hash_dict.get(n[i],0)+1
for x in m:
    print(hash_dict.get(x,0))

# Character Hashing

S = "aannxxccggjsyyvbx"
q = ["a", "x", "s", "b"]

hash_dict = {}

for i in range(0,len(S)):
    hash_dict[S[i]] = hash_dict.get(S[i],0)+1
for char in q:
    print(hash_dict.get(char,0))


# Time Complexity -> O(N+M)
# Space Complexity -> O(1)