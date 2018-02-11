class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        num = str(x)
        length = len(num)
        start = 0
        reverse_str = ''
        if num[0]=='-':
            reverse_str += '-'
            start += 1
        if num[len(num)-1]=='0':
            length -= 1
        
        for j in range(length-1,start-1,-1):
            reverse_str += num[j]
        
        reverse_num = int(reverse_str)
        if reverse_num > (1<<31)-1 or reverse_num < - (1<<31):
            return 0

        return reverse_num

if __name__=="__main__":
    num1 = 123
    num2 = -123
    num3 = 120
    result1 = Solution().reverse(num1)
    result2 = Solution().reverse(num2)
    result3 = Solution().reverse(num3)
    print(result1,result2,result3)
         
