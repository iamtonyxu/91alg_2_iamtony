# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    obj = Solution()
    head = obj.reverseList(head)

    while head:
        print(head.val)
        head = head.next

