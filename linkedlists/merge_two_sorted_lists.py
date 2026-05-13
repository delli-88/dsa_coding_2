from singly_linked_list import ListNode, LinkedList
class Solution:
    def mergeTwoLists(self, list1, list2):
        list1 = LinkedList().createLinkedList(list1)
        list2 = LinkedList().createLinkedList(list2)

        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next

sol = Solution()
print(sol.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))