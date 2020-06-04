# Given a non-empty, singly linked list with head node 'head', this function returns a middle node of linked list. If there are two middle nodes, it returns the second node.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = head
        i = 0
        while(tmp.next):
            i += 1
            tmp = tmp.next
        i += 1
        i = i//2
        print(i)
        node = head
        while(i>0):
            node = node.next
            i -= 1
        return node
