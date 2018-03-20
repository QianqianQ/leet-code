#include <stdlib.h>
#include <iostream>
#include <initializer_list>
// Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

ListNode *LinkedList(std::initializer_list<int> l)
{
	auto iter = l.begin();
	ListNode *head = l.size() ? new ListNode(*iter++):NULL;
	for (ListNode *current = head; iter != l.end(); current = current->next) {
		current->next = new ListNode(*iter++);
	}
	return head;
}

class Solution {
public:
	ListNode * addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode *dummy = NULL;
		ListNode *current = NULL;
		int carry = 0;
		auto p = l1, q = l2;
		while (p != NULL || q != NULL)
		{
			int x = p ? p->val:0;
			int y = q ? q->val:0;
			int sum = x + y + carry;
			ListNode *node = new ListNode{ sum % 10 };
			if (!dummy)
			{
				dummy = node;
				current = dummy;
			}
			else
			{
				current->next = node;
				current = current->next;
			}
			carry = sum / 10;
			if (p != NULL){
				p = p->next;
			}
			if (q != NULL) {
				q = q->next;
			}
		}
		if (carry != 0){
			current->next = new ListNode{ carry };
		}
		return dummy;

	}
};

int main(void)
{
	Solution s;
	ListNode* l1 = LinkedList({ 2,4,3 });
	ListNode* l2 = LinkedList({ 5,6,4 });
	ListNode* result = s.addTwoNumbers(l1, l2);
	for (ListNode *current = result; current; current=current->next)
	{
		std::cout << current->val;
	}
	return 0;
}
