from math import floor
class Solution:
    
    def reverse(self, x: int) -> int: 
        if x >= (2**31)-1 or x <= -2**31: 
            return 0 

        reverse = str(x)[::-1] 
        if reverse[0] == '0' and len(reverse)>1: 
             reverse = reverse[1:] 
        if reverse[-1] == '-': 
            reverse = '-'+reverse[:-1] 
        if int(reverse) >= (2**31)-1 or int(reverse) <= -2**31: 
            return 0 
        return int(reverse)

if __name__=="__main__":
    num1 = 123
    num2 = -123
    num3 = 120
    # result1 = Solution().reverse2(num1)
    # result2 = Solution().reverse2(num2)
    # result3 = Solution().reverse2(num3)
    import os
    os.link('7_reverseInteger.py','test.py')
    os.link('test.py','test1.py')
    os.unlink('test.py')
         
