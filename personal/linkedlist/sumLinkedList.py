'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None

        current = l1
        val1 = ""
        while current:
            val1 = str(current.val) + val1
            current = current.next
        
        current = l2
        val2 = ""
        while current:
            val2 = str(current.val) + val2
            current = current.next
        result = str(int(val1) + int(val2))
        return (self.createLinkedList(result[::-1]))
    
    def createLinkedList(self, val) -> ListNode:

        head = ListNode(val[0])
        current = head

        for num in val[1:]:
            current.next = ListNode(num)
            current = current.next
        
        return head

    
    def printLinkedList(self, head) -> bool:
        current = head

        while current:
            print(current.val)
            current = current.next
        return True


soln: Solution = Solution()
list1 = soln.createLinkedList([2,4,3, 2])
list2 = soln.createLinkedList([5,6,4])

sum = soln.addTwoNumbers(list1, list2)
soln.printLinkedList(sum)
        
