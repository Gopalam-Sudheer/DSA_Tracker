# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        temp=head
        prev=None
        while temp.val in s:
            temp=temp.next
            head=temp
        while temp:
            if temp.val in s:
                prev.next=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
        return head