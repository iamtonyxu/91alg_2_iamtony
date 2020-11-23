from typing import List

class Solution:
	def permutation(self, words):
		if len(words) <= 1:
			return words
		l = [] # empty list that will store current permutation
		for i in range(len(words)):
			m = words[i]
			# Extract words[i] from the list. reminderWords is remaining list
			remainWords = words[:i] + words[i+1:]
			#Generating all permutations where m is the first element
			for p in self.permutation(remainWords):
				l.append(m + p)
		return l

	def findSubstring(self, s: str, words: List[str]) -> List[int]:
		wordString = []
		for subset in self.permutation(words):
			wordString.append(subset)

		location = []
		for subString in wordString:
			loc = s.find(subString)
			if loc == -1:
				pass
			else:
				location.append(loc)
		return location


if __name__ == '__main__':
	solution = Solution()
	#s = "barfoothefoobarman"
	#words = ["foo", "bar"]
	s = "wordgoodgoodgoodbestword"
	words = ["word", "good", "best", "good"]
	res = solution.findSubstring(s, words)
	for i in res:
		print(i)