
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
        #The node for the new value I want to add
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
        
        #after getting to the end, now add the new node
        current.next = newNode
        
        #return the head. it'll be a reference to the whole list
        return head


head = None

soln: Solution = Solution()

head = soln.addToLinkiedList(head, 30)
head = soln.addToLinkiedList(head, 20)
head = soln.addToLinkiedList(head, 10)

soln.printLinkedList(head)
print(soln.hasCycle(head))

