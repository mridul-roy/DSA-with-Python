class Solution(object):
    def reverse(self, x):
        negative = x < 0 
        x = abs(x)
        
        revers_num = self.helper(x, len(str(x))-1)
        
        if negative :
            revers_num = -revers_num
            
        if revers_num < -2147483648 or revers_num > 2147483647:
            return 0
        return revers_num
    def helper(self,x,power):
        if x < 10:
            return x
        return (x%10)*(10**power) + self.helper(x//10, power -1)
    

obj = Solution()
print(obj.reverse(1234))