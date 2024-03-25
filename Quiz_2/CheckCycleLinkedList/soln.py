
class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
    
class Solution:
    def hasCycle(self, head:Node) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    

    #INFO: THE FOLLOWING CODE WAS JUST MEANT TO TEST THE hasCycle() METHOD
    
    def printLinkedList(self, head: Node):
        if not head:
            return None
        
        current = head
        while current:
            print(current.val)
            current = current.next

        
    def addToLinkiedList(self, head, val):
        newNode = Node(val)
        #check isthe head exists, if not, ill make a new node
        if not head:
            head = newNode
            return head

        #loop through all the values in the linkedlist to the end. 
        #I feel a cycle in a linked list will very quickly get this into an infinite loop
        current = head
        while current.next:
            current = current.next
        
        current.next = newNode
        return head
    
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

soln: Solution = Solution()

# head = soln.addToLinkiedList(head, 30)
# head = soln.addToLinkiedList(head, 20)
# head = soln.addToLinkiedList(head, 10)

head = soln.createCycleLinkedList([1, 2, 3, 4, 5], 3)

#soln.printLinkedList(head)
print(soln.hasCycle(head)) #Prints out true

