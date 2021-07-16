# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


def genListNode(numList: list) -> ListNode:
    ans = ListNode(float('-inf'))
    node = ans
    for num in numList:
        node.next = ListNode(num)
        node = node.next
    return ans.next