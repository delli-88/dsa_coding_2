import linkedlist_implementation

class Solution:
    def reverseList(self, head):

        # head = linkedlist_implementation.LinkedList().createLinkedList(head)
        if head == None or head.next == None:
            return head

        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

sol = Solution()
print(sol.reverseList(head = [1,2,3,4,5]))