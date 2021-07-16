'''
给你链表的头结点head，请将其按 升序 排列并返回 排序后的链表 。
进阶：
你可以在O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
Example-1
输入：head = [4,2,1,3]
输出：[1,2,3,4]
Example-2
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
'''

from ListNodePkg import ListNode, genListNode

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 遍历链表，node.val保存到val_list
        cur = head
        val_list = []
        while cur:
            val_list.append(cur.val)
            cur = cur.next
        # 排序
        val_list.sort()
        # 生成新的链表
        dummy = new_head = ListNode(-1)
        for val in val_list:
            new_head.next = ListNode(val)
            new_head = new_head.next
        # 返回结果
        return dummy.next


if __name__ == "__main__":
    numList1 = [4, 3, 2, 1, 4]
    list1 = genListNode(numList1)

    obj = Solution()
    list2 = obj.sortList(list1)
    head = list2
    while head:
        print(head.val)
        head = head.next