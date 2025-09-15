# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(curr):
            if curr==None or curr.next==None:
                return curr
            prev=None
            nex=None
            while curr!=None:
                nex=curr.next
                curr.next=prev
                prev=curr
                curr=nex
            return prev
        if head==None or head.next==None:
            return True
        slow=head
        fast=head.next
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        if fast.next!=None:
            fast=fast.next
        fast=reverse(slow.next)
        slow=head
        while slow!=None and fast!=None:
            if slow.val!=fast.val:
                return False
            slow=slow.next
            fast=fast.next
        return True