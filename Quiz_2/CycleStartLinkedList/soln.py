class Node:
    def __init__ (self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def detectCycle(self, head):

        if not head:
            return None
        if head.next is None:
            return None

        slow = head
        fast = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        # want to see if the loop was broken by fast or fast.next being null,  not slow=fast
        if not fast and fast.next:
            return None
        
        #Happens if slow is moved to the start and both pointers move at the same speed, theyll meet at the cycle
        slow = head
        count = 0 # Count how many nodes deep the cycle is at
        while slow != fast:
            slow = slow.next
            fast = fast.next
            count += 1

        return count
    
    def createCycleLinkedList(self, values, pos):
        if not values:
            return None
        
        # Create the linked list without a cycle
        head = Node(values[0])
        current = head
        for val in values[1:]:
            current.next = Node(val)
            current = current.next
        
        # If pos is valid, create a cycle by finding the node at position pos
        # and connecting it to the tail of the linked list
        if pos < len(values):
            cycle_node = head
            for i in range(pos):
                cycle_node = cycle_node.next
            current.next = cycle_node
        return head


head = None
soln: Solution = Solution

head = soln.createCycleLinkedList(soln, [1, 2, 3, 8, 5], 3)

print(soln.detectCycle(soln, head)) #Prints out 8, the 3rd node (counted from 0)