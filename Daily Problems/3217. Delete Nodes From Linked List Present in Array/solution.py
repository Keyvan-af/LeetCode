# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
            # Convert nums to a set for O(1) lookups
            to_remove = set(nums)
            
            # Create a dummy node to handle the case where the head needs to be removed
            dummy = ListNode(0)
            dummy.next = head
            
            # Previous and current pointers for traversal
            prev, curr = dummy, head
            
            # Traverse the list
            while curr:
                if curr.val in to_remove:
                    # Remove the current node
                    prev.next = curr.next
                else:
                    # Move prev pointer only if current node is not removed
                    prev = curr
                # Move to the next node
                curr = curr.next
            
            # Return the new head (dummy.next)
            return dummy.next