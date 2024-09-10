# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current is not None and current.next is not None:

            gcd_value = math.gcd(current.val, current.next.val)
            gcd_node = ListNode(gcd_value)
            
            # Insert the GCD node between current and current.next
            gcd_node.next = current.next
            current.next = gcd_node
            
            # Move the current pointer two steps ahead (to skip the newly inserted GCD node)
            current = gcd_node.next
        return head