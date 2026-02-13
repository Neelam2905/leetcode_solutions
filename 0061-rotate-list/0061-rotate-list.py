# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return head

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        n=len(nodes)
        k=k%n
        if k==0:
            return head

        new_head=nodes[n-k]
        nodes[n-k-1].next=None
        nodes[-1].next=head

        return new_head