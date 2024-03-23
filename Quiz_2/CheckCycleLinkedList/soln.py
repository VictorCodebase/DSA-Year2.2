
class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
    
class Solution:
    def hasCycle(self, head:Node) -> bool:
        slow, fast = head, head

        while fast and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

