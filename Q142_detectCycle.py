'''
给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。
进阶：
你是否可以使用 O(1) 空间解决此题？
Example-1.
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
Example-2.
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
Example-3.
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
'''

from ListNodePkg import ListNode, genListNode

class Solution:
    def detectCycle_v1(self, head: ListNode) -> ListNode:
        # hashTable
        hashTable = set()
        cur = head
        while cur:
            if cur in hashTable:
                return cur
            else:
                hashTable.add(cur)
                cur = cur.next
        return None

    def detectCycle_v2(self, head: ListNode) -> ListNode:
        # fast/slow pointer method
        fast = slow = head
        while True:
            if fast and fast.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next
            if slow == fast:
                break

        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast


if __name__ == "__main__":
    numList1 = [1, 2, 3]
    List1 = genListNode(numList1)
    head, tail = List1, None
    while head:
        print(head.val)
        tail = head
        head = head.next
    tail.next = List1

    obj = Solution()
    cycleStartNode = obj.detectCycle_v1(List1)
    print(cycleStartNode.val)


    cycleStartNode = obj.detectCycle_v2(List1)
    print(cycleStartNode.val)

