# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time complexity: O(max(m,n)), Space complexity: O(max(m,n))
    def addTwoNumbers(self,l1,l2):
        dummy = ListNode(0)
        carry = 0
        p = l1
        q = l2
        current = dummy
        while (p is not None) or (q is not None):
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = x + y + carry
            current.next = ListNode(sum % 10)
            current = current.next
            carry = sum // 10
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy.next

class Solution2:
    
    def getNum(self,l: ListNode) -> int:
        ele = 0
        value = 0
        while l is not None:
            value += l.val*(10**ele)
            ele += 1
            l = l.next
        return value
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value1 = self.getNum(l1)
        print(value1)
        value2 = self.getNum(l2)
        print(value2)
        total = value1 + value2
        digits = [int(i) for i in str(total)][::-1]
        print(digits)
        res = list()
        res.append(ListNode(digits[0]))
        for i in digits[1:]:
            new_node = ListNode(i)
            res[-1].next = new_node
            res.append(new_node)
        
        return res[0]

if __name__=="__main__":
    l1, l1.next, l1.next.next = ListNode(2), ListNode(4), ListNode(3)
    l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(l1,l2)
    print(result.val,result.next.val,result.next.next.val)

        



