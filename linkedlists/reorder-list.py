import singly_linked_list
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head = singly_linked_list.LinkedList().createLinkedList(head)
        
        if not head or not head.next:
            return head

        mid = self.getMid(head)

        second = mid.next
        mid.next = None
        second = self.reverseList(second)

        first = head
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        return head

    def getMid(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

sol = Solution()
print(sol.reorderList(head = [1,2,3,4,5]))