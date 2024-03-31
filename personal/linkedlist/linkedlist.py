class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedLists:
    def createLinkedList(self, list):
        if not list:
            return False
        
        head = Node(list[0]) #dont lose the head
        current = head
        for val in list[1:]:
            current.next = Node(val)
            current = current.next
        return head
    
    def readLinkedList(self, head:Node) -> bool:
        if not head:
            return False
        
        current = head
        while current:
            print(current.val)
            current = current.next
        return True

example:LinkedLists = LinkedLists()

example.readLinkedList(example.createLinkedList([3, 4, 2, 1, 9, 5]))


        


