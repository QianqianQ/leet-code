/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode(0);
    let carry = 0;
    let current = dummy;
    while (l1 !== null || l2 !== null){
        x = (l1 !== null) ? l1.val : 0;
        y = (l2 !== null) ? l2.val : 0;
        sum = x+y+carry;
        current.next = new ListNode(sum % 10);
        current = current.next;
        carry = Math.floor(sum / 10);
        if (l1 !== null){
            l1 = l1.next;
        }
        if (l2 !== null){
            l2 = l2.next;
        }
    }
    if (carry === 1){
        current.next = new ListNode(carry);
    }
    return dummy.next;
};

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers2 = function(l1, l2) {
    let dummy = new ListNode(0);
    let carry = 0;
    let current = dummy;
    while (l1 !== null || l2 !== null){
        x = (l1 !== null) ? l1.val : 0;
        y = (l2 !== null) ? l2.val : 0;
        sum = x+y+carry;
        current.next = new ListNode(sum % 10);
        current = current.next;
        carry = Math.floor(sum / 10);
        if (l1 !== null){
            l1 = l1.next;
        }
        if (l2 !== null){
            l2 = l2.next;
        }
    }
    if (carry === 1){
        current.next = new ListNode(carry);
    }
    return dummy.next;
};

const l1 = new ListNode(2);
l1.next = new ListNode(4);
l1.next.next = new ListNode(3);

const l2 = new ListNode(5);
l2.next = new ListNode(6);
l2.next.next = new ListNode(4);

const l3 = addTwoNumbers(l1,l2);
console.log(l3.val, l3.next.val, l3.next.next.val);