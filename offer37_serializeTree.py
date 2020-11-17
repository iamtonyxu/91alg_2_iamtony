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
		# preorder
		if not root: return '#'
		return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		:type data: str
		:rtype: TreeNode
		"""
		def helper(data):
			if data[0] == '#':
				data.popleft()
				return None
			tmp = data.popleft()
			root = TreeNode(int(tmp))
			root.left = helper(data)
			root.right = helper(data)
			return root

		data = collections.deque(data.split(','))
		return helper(data)


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
