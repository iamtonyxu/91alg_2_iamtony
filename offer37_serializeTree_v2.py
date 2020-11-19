import collections

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Codec:
	def serialize(self, root):
		"""Encodes a tree to a single string.
		:type root: TreeNode
		:rtype: str
		"""
		# 层次遍历
		if not root: return '#'
		dq, res = collections.deque(), []
		dq.append(root)
		while dq:
			dq_len = len(dq)
			layer = []
			while dq_len > 0:
				dq_len -= 1
				node = dq.popleft()
				if not node:
					layer.append('#')
				else:
					layer.append(str(node.val))
					dq.append(node.left)
					dq.append(node.right)
			res.extend(layer)
		return res


	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		:type data: str
		:rtype: TreeNode
		"""
		if data is None or len(data)==0 or data[0] == "null":
			return None
		root = TreeNode(data[0])
		index = 1
		q = collections.deque()
		q.append(root)
		while q:
			curNode = q.popleft()
			if curNode is None:
				continue
			if data[index] == "#":
				curNode.left = None
			else:
				curNode.left = TreeNode(data[index])
			index += 1 # get right node index
			if data[index] == "#":
				curNode.right = None
			else:
				curNode.right = TreeNode(data[index])
			index += 1 # move to nextNode's left
			q.append(curNode.left)
			q.append(curNode.right)
		return root


if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.right.left = TreeNode(4)
	root.right.right = TreeNode(5)

	codec = Codec()
	tree_str = codec.serialize(root)
	print(tree_str)
	root_generated = codec.deserialize(tree_str)
	print('Done')
