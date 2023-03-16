class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_node = ListNode()
        pointer = merged_node

        current1 = list1
        current2 = list2

        while current1 is not None or current2 is not None:
            if current1 is None:
                pointer.next = ListNode(current2.val)
                pointer = pointer.next
                current2 = current2.next
            elif current2 is None:
                pointer.next = ListNode(current1.val)
                pointer = pointer.next
                current1 = current1.next
            else:
                if current1.val <= current2.val:
                    pointer.next = ListNode(current1.val)
                    pointer = pointer.next
                    current1 = current1.next
                else:
                    pointer.next = ListNode(current2.val)
                    pointer = pointer.next
                    current2 = current2.next

        return merged_node.next