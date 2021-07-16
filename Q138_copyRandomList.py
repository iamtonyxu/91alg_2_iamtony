import copy

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # deepcopy
        return copy.deepcopy(head)

    def copyRandomList_v2(self, head: 'Node') -> 'Node':
        dummy = new_head = Node(-1)
        # 第一次遍历：生成所有节点，将各个节点val和next拷贝;
        # 同时将新旧节点分别保存到数组list1和list2,为第二步拷贝random准备
        cur = head
        list1, list2 = [], []
        while cur:
            new_head.next = Node(cur.val, None, None)
            new_head = new_head.next
            list1.append(new_head)
            list2.append(cur)
            cur = cur.next
        # 第二次遍历：拷贝各个节点random
        cur = head
        new_head = dummy.next
        while cur:
            if cur.random in list2:
                index = list2.index(cur.random)
                new_head.random = list1[index]
            else:
                new_head.random = None
            cur = cur.next
            new_head = new_head.next
        return dummy.next

    '''
    # ERROR: Random pointer of node with label 13 points to a node from the original list.
    def copyRandomList_v2(self, head: 'Node') -> 'Node':
        # 遍历所有节点，依次拷贝val, next, random
        dummy = new_head = Node(float('-inf'))
        while head:
            new_head.next = Node(head.val, head.next, head.random)
            new_head = new_head.next
            head = head.next
        return dummy.next
    '''