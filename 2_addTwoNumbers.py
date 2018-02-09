# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i1,i2 = 0,0
        l1_num, l2_num = 0,0

        while l1.next is not None:
            l1_num += l1.val*10**i1
            i1+= 1
            l1 = l1.next
        l1_num += l1.val*10**i1
        
        while l2.next is not None:
            l2_num += l2.val*10**i2
            i2 += 1
            l2 = l2.next
        l2_num += l2.val*10**i2

        print(l1_num,l2_num)
        sum = l1_num+l2_num

        if sum<10:
            result = ListNode(sum)
            return result
        else:
            temp = sum % 10
            result = ListNode(temp)
            first = result 
        
        sum = sum // 10
        while sum >=10:
            temp = sum % 10
            result.next = ListNode(temp)
            result = result.next
            sum = sum // 10
        
        result.next = ListNode(sum)

        return first

if __name__=="__main__":
    l1, l1.next, l1.next.next = ListNode(2), ListNode(4), ListNode(3)
    l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(l1,l2)
    print(result.val,result.next.val,result.next.next.val)

        



