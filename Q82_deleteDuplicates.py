'''
存在一个按升序排列的链表, 给你这个链表的头节点 head, 请你删除链表中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。
返回同样按升序排列的结果链表。
Example-1.
输入: [1, 1, 2, 3, 3, 4]
输出：[2, 4]
'''

from ListNodePkg import ListNode, genListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        nodeCount = {}
        # calculate counts of each node in the list
        while head:
            if head.val in nodeCount:
                nodeCount[head.val] += 1
            else:
                nodeCount[head.val] = 1
            head = head.next

        # create a new list to add the node whose count is 1
        dummy = head = ListNode(float('-inf'))
        for (key, count) in nodeCount.items():
            if count == 1:
                head.next = ListNode(key)
                head = head.next
        return dummy.next

    def deleteDuplicates_v2(self, head: ListNode) -> ListNode:
        # one iteration
        dummy = ListNode(float('-inf'))
        dummy.next = head

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


if __name__ == "__main__":
    numList1 = [1, 1, 1, 2, 3, 3, 3, 4, 5]
    list1 = genListNode(numList1)

    obj = Solution()
    list2 = obj.deleteDuplicates(list1)
    head = list2
    while head:
        print(head.val)
        head = head.next

    numList1 = [1, 1, 1, 2, 3, 3, 3, 4, 5]
    list1 = genListNode(numList1)

    list2 = obj.deleteDuplicates_v2(list1)
    head = list2
    while head:
        print(head.val)
        head = head.next