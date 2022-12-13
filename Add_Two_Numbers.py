'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        curr_node = result
        a=0
        while l1!=None and l2!=None:
            s = l1.val + l2.val + a
            new_node = ListNode(s%10)
            curr_node.next = new_node
            curr_node = new_node
            a = s//10
            l1=l1.next
            l2=l2.next
        
        if l1==None and l2==None:
            if a>0:
                new_node = ListNode(a)
                curr_node.next = new_node
                curr_node = new_node
        elif l1!=None:
            while l1!=None:
                s = l1.val + a
                new_node = ListNode(s%10)
                curr_node.next = new_node
                curr_node = new_node
                a = s//10
                l1=l1.next
            if a>0:
                new_node = ListNode(a)
                curr_node.next = new_node
                curr_node = new_node
        elif l2!=None:
            while l2!=None:
                s = l2.val + a
                new_node = ListNode(s%10)
                curr_node.next = new_node
                curr_node = new_node
                a = s//10
                l2=l2.next
            if a>0:
                new_node = ListNode(a)
                curr_node.next = new_node
                curr_node = new_node
        return result.next