from typing import List


class Solution:
	def numberOfBoomerangs(self, points: List[List[int]]) -> int:
		res = 0
		for i in range(len(points)):
			hashTable = {}
			for j in range(len(points)):
				if i != j:
					distance = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + \
					           (points[i][1] - points[j][1]) * (points[i][1] - points[j][1])
					if distance not in hashTable:
						hashTable[distance] = 1
					else:
						# // 每增加一个，就多2 * t个组合配对，例如原来一个，现增加一个，则增加2个组合；若原有两个，则增加一个，新增的与原有的每个进行排列都会增加两个组合，依次类推
						res += 2 * hashTable[distance]
						hashTable[distance] += 1
		return res


if __name__ == '__main__':
	solution = Solution()
	#points = [[1, 0], [0, 0], [2, 0]]
	points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
	res = solution.numberOfBoomerangs(points)
	print(res)
