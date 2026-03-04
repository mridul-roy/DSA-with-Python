class Solution(object):
    def isPalindrome(self, x):

        num = x
        result = 0
        while num>0:
            last_digit = num%10
            result = (result*10)+last_digit
            num= num//10


        if x == result:
            return True
        else:
            return False
        
        
new_Solution=Solution() 
     
print(new_Solution.isPalindrome(121))