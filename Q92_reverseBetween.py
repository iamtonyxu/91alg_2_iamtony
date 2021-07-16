'''
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
Example-1:
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
Example-2:
输入：head = [5], left = 1, right = 1
输出：[5]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        now, prev = head, None
        i = 1
        reverse_start, reverse_end = None, None
        while i < left:
            prev = now
            now = now.next
            i += 1

        reverse_start = prev
        reverse_end = now

        while now and i <= right:
            next = now.next
            now.next = prev
            prev = now
            now = next
            i += 1

        if left == 1:
            head = prev
        else:
            reverse_start.next = prev
        reverse_end.next = now

        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)



    obj = Solution()
    head = obj.reverseBetween(head, 1, 4)

    while head:
        print(head.val)
        head = head.next