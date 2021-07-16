'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
Example-1.
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

Example-2.
输入：l1 = [], l2 = []
输出：[]

Example-3.
输入：l1 = [], l2 = [0]
输出：[0]
'''

from ListNodePkg import ListNode, genListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(-1)
        cur = ans
        while l1 and l2:
            cur.next = ListNode(min(l1.val, l2.val))
            cur = cur.next
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return ans.next


def unitTest(numList1: list, numList2: list):
    l1, l2 = genListNode(numList1), genListNode(numList2)

    obj = Solution()
    l3 = obj.mergeTwoLists(l1, l2)

    while l3:
        print(l3.val)
        l3 = l3.next


if __name__ == "__main__":
    numList1, numList2 = [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]
    unitTest(numList1, numList2)

    numList1, numList2 = [], []
    unitTest(numList1, numList2)

    numList1, numList2 = [], [1]
    unitTest(numList1, numList2)
