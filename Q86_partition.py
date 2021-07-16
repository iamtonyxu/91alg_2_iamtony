'''
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置。

Example-1.
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

Example-2.
输入：head = [2,1], x = 2
输出：[1,2]

'''

from ListNodePkg import ListNode, genListNode

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 遍历所有节点：
        # (1)所有小于x的节点放在新链表list1
        # (2)所有大于或等于x的节点都放在新链表list2
        # (3)list1的尾节点指向list2的头节点
        dummy1 = head1 = ListNode(float('-inf'))
        dummy2 = head2 = ListNode(float('-inf'))
        while head:
            if head.val < x:
                head1.next = ListNode(head.val)
                head1 = head1.next
            else:
                head2.next = ListNode(head.val)
                head2 = head2.next
            head = head.next
        head1.next = dummy2.next
        return dummy1.next


if __name__ == "__main__":
    numList = [[1, 4, 3, 2, 5, 2], [2, 1]]

    for nums in numList:
        list1 = genListNode(nums)
        obj = Solution()
        list2 = obj.partition(list1, 3)
        head = list2
        while head:
            print(head.val)
            head = head.next


