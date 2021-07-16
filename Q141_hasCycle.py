from ListNodePkg import ListNode, genListNode


class Solution:
    def hasCycle_v1(self, head: ListNode) -> bool:
        hashTable = set()
        while head:
            if head in hashTable:
                return True
            else:
                hashTable.add(head)
                head = head.next
        return False

    def hasCycle_v2(self, head: ListNode) -> bool:
        # fast/slow pointers
        fast = slow = head
        # the speed of fast / slow pointer is 2 / 1
        # check the first meeting time
        while True:
            if fast and fast.next:
                fast = fast.next.next
            else:
                fast = None
                break
            slow = slow.next
            if fast == slow:
                break
        # return result
        return True if fast else False


if __name__ == "__main__":
    numList1 = [1, 2, 3]
    List1 = genListNode(numList1)
    head, tail = List1, None
    while head:
        print(head.val)
        tail = head
        head = head.next
    tail.next = List1.next

    obj = Solution()
    itHasCycle = obj.hasCycle_v1(List1)
    print(itHasCycle)

    itHasCycle = obj.hasCycle_v2(List1)
    print(itHasCycle)
