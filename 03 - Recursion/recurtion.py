# Print Name 5 times

def call_name():
    for i in range(0,5):
     print("ARNOB")
     
     
call_name()

## Print with Recursion
count = 0

def call_name():
    global count
    if count == 5:
        return
    print("ARNOB")
    count+=1

    call_name()
    
call_name()

# Print with Recursion with Parameters

def func(x,N):
    if N == 0:
        return
    print(x)
    func(x,N-1)
    
func(15,5)

# Print 1 to N with recursion

def func(i,N):
    if i > N:
        return
    print(i)
    func(i+1,N)

func(1,15)