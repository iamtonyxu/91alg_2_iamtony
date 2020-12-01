# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def middleNode(self, head: ListNode) -> ListNode:
		fast = slow = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		return slow


if __name__ == "__main__":
	head = ListNode(1)
	'''
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
	'''
	solution = Solution()
	mid = solution.middleNode(head)
	while mid:
		print(mid.val)
		mid = mid.next