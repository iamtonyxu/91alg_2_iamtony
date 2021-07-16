'''
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

from ListNodePkg import ListNode, genListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Iteration 1, put node.val in a list
        cur = head
        val_list = []
        while cur:
            val_list.append(cur.val)
            cur = cur.next
        # Check val_list[i] == val_list[n - i - 1]
        len_of_list = len(val_list)
        for i in range(len_of_list//2):
            if val_list[i] != val_list[len_of_list - i - 1]:
                return False
        return True


if __name__ == "__main__":
    numList1 = [1, 2, 2, 1]
    list1 = genListNode(numList1)

    obj = Solution()
    isPd = obj.isPalindrome(list1)
    if isPd:
        print("This List is palindrome.")
    else:
        print("This List is NOT palindrome.")
