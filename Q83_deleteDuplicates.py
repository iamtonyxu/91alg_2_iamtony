from ListNodePkg import ListNode, genListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev, now = ListNode(float('-inf')), head
        prev.next = now
        nodeTable = set()
        while now:
            if now.val in nodeTable:
                prev.next = now.next
            else:
                prev = now
                nodeTable.add(now.val)
            now = now.next
        return head

    def deleteDuplicates_v2(self, head: ListNode) -> ListNode:
        # fast/slow pointer method
        dummy = ListNode(float('-inf'))
        dummy.next = head
        slow, fast = dummy, head
        while fast:
            if slow.val != fast.val:
                slow = slow.next
                fast = fast.next
            else:
                fast = fast.next
                slow.next = fast
        return dummy.next


if __name__ == "__main__":
    numList1 = [1, 1, 1, 1, 2, 2, 3]
    list1 = genListNode(numList1)

    obj = Solution()
    list2 = obj.deleteDuplicates(list1)
    head = list2
    while head:
        print(head.val)
        head = head.next

    numList1 = [1, 1, 1, 1]
    list1 = genListNode(numList1)
    list3 = obj.deleteDuplicates_v2(list1)
    head = list3
    while head:
        print(head.val)
        head = head.next

