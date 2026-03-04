###_____Parameterized and Functional Recursion_______##

def func(sum,i,N):
    if i>N:
        print(sum)
        return
    func(sum+i,i+1,N)
    
func(0,1,10)

# Time complexity O(N)

# Functional Recursion

def func(N):
    if N==1:
        return 1
    return (N+func(N-1))

print(func(10))

## Time complexity O(N)


##Factorial With Functional Recursion


def func(n):
    if n == 1:
        return 1
    return (n*func(n-1))

print(func(10))

## Time complexity O(N)
## Space complexity o(N)--> Stack Space