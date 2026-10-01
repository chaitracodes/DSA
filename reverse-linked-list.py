# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            next_node = curr.next             #save
            curr.next = prev                  #reverse         
            prev = curr                       #move prev
            curr = next_node                  #move curr
        return prev