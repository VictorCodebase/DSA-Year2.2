class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class LinkedList:

    def createLinkedList(self, list):
        head = Node(list[0])

        current = head
        for val in list[1:]:
            current.next = Node(val)
            current = current.next
        return head
        
    def printLinkedList(self, head):

        current = head
        while current:
            print (current.val)
            current = current.next

    def reverseLinkedList(self, head):
        #use two pointers
        prev = None
        current = head

        while current:
            tempNext = current.next
            current.next = prev
            prev = current
            current = tempNext
        return prev #loops stops executing when the previous is current (now head) and the next is null

linkedlist: LinkedList = LinkedList()

newLinkedList = linkedlist.createLinkedList([3, 56, 32, 90, 12, 34, 100])
linkedlist.printLinkedList(newLinkedList)
