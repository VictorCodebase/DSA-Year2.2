class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
    def createLinkedList(self, list):
            if not list:
                return False
            
            head = ListNode(list[0]) #dont lose the head
            current = head
            for val in list[1:]:
                current.next = ListNode(val)
                current = current.next
            return head

    def readLinkedList(self, head:ListNode) -> bool:
        if not head:
            return False
        
        current = head
        while current:
            print(current.val)
            current = current.next
        return True


example:LinkedList = LinkedList()

linkedlist = example.createLinkedList([2, 45, 65, 2, 4])
reversedLinkedList = example.reverseLinkedList(linkedlist)
example.readLinkedList(reversedLinkedList)
