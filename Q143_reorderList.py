'''
给定一个单链表L：L0 → L1 → … → Ln-1 → Ln ，
将其重新排列后变为： L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.

示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
'''

from ListNodePkg import ListNode, genListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # iteration 1, put nodes in a list
        cur = head
        list1 = []
        while cur:
            list1.append(cur)
            cur = cur.next
        # iteration 2, reorder the list
        for i in range(len(list1)//2):
            node = list1[i]
            temp = node.next
            node.next = list1[len(list1) - i - 1]
            node.next.next = temp
        list1[len(list1)//2].next = None

        return head


if __name__ == "__main__":
    numList1 = [1, 2, 3, 4]
    list1 = genListNode(numList1)

    obj = Solution()
    obj.reorderList(list1)
    head = list1
    while head:
        print(head.val)
        head = head.next