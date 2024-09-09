# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the matrix filled with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Directions for spiral order traversal (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        
        # Boundaries for the spiral traversal
        top, bottom, left, right = 0, m - 1, 0, n - 1
        row, col = 0, 0
        
        current_node = head
        
        # Traverse the matrix in spiral order
        while current_node:
            matrix[row][col] = current_node.val
            current_node = current_node.next
            
            # Move in the current direction
            next_row = row + directions[current_direction][0]
            next_col = col + directions[current_direction][1]
            
            # Check if we need to change direction
            if not (top <= next_row <= bottom and left <= next_col <= right):
                # Adjust boundaries and change direction
                if current_direction == 0:  # Moving right
                    top += 1
                elif current_direction == 1:  # Moving down
                    right -= 1
                elif current_direction == 2:  # Moving left
                    bottom -= 1
                elif current_direction == 3:  # Moving up
                    left += 1
                
                # Change direction clockwise
                current_direction = (current_direction + 1) % 4
                
            # Update row and col to the next position
            row += directions[current_direction][0]
            col += directions[current_direction][1]
        
        return matrix
