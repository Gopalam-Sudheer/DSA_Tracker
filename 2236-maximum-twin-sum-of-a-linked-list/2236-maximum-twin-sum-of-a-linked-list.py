# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        prev=None
        cur=slow
        nex=slow
        while nex:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        start=head
        end=prev
        ans=0
        while end:
            ans=max(ans,start.val+end.val)
            start=start.next
            end=end.next
        return ans
