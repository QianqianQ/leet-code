class Solution:
    def reverse(self,x):
        if x<0:
            return -self.reverse(-x)
        else:
            reversed = int(str(x)[::-1])

        return reversed if x <= 0x7fffffff else 0

if __name__=="__main__":
    num1 = 123
    num2 = -123
    num3 = 120
    result1 = Solution().reverse(num1)
    result2 = Solution().reverse(num2)
    result3 = Solution().reverse(num3)
    print(result1,result2,result3)
         
