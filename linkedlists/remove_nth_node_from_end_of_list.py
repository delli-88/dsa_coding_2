from singly_linked_list import ListNode, LinkedList
class Solution:
    def removeNthFromEnd(self, head, n) :
        head = LinkedList().createLinkedList(head)
        
        dummy = ListNode(-1)
        dummy.next = head

        first = dummy
        second = dummy

        for _ in range(n+1):
            second = second.next
        
        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        
        return dummy.next

sol = Solution()
print(sol.removeNthFromEnd(head = [1,2,3,4,5], n=2))