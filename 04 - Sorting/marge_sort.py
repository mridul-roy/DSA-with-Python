left = [3,5,6]
right = [2,3,5,6,7,9]

def marge_arr(left,right):
    result = []
    i,j = 0,0
    n,m = len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    while i<n:
        result.append(left[i])
        i+=1
        
    while j<m:
        result.append(right[j])
        j+=1
    return result
    
print(marge_arr(left,right))