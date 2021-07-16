'''
给定两个由小写字母构成的字符串 A 和 B，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回true；否则返回 false 。
交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad"

示例 1：
输入： A = "ab", B = "ba"
输出： true
解释： 你可以交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 相等。

示例 2：
输入： A = "ab", B = "ab"
输出： false
解释： 你只能交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 不相等。

示例 3:
输入： A = "aa", B = "aa"
输出： true
解释： 你可以交换 A[0] = 'a' 和 A[1] = 'a' 生成 "aa"，此时 A 和 B 相等。

示例 4：
输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true

示例 5：
输入： A = "", B = "aa"
输出： false
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        '''
        # swap(s[i], s[j]) and save the new str as d
        # compare d with goal and return the result
        for i in range(len(s)):
            for j in range(i, len(s)):
                d = s[0:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                if d == goal: return True
        return False
        '''
        if len(s) != len(goal): return False
        if s == goal:
            ss = set()
            for c in s:
                if c in ss: return True
                ss.add(c)
            return False

        # find the indexes(should be 2) of diff
        p = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                p.append(i)
        if len(p) == 2:
            if s[p[0]] == goal[p[1]] and s[p[1]] == goal[p[0]]: return True
        return False


if __name__ == "__main__":
    obj = Solution()
    A, B= "ab", "ba"
    print(obj.buddyStrings(A, B))

    A, B= "ab", "ab"
    print(obj.buddyStrings(A, B))

    A, B= "aaaaaaabc", "aaaaaaacb"
    print(obj.buddyStrings(A, B))

    A, B= "", "aa"
    print(obj.buddyStrings(A, B))

    A, B= "aa", "aa"
    print(obj.buddyStrings(A, B))

    A, B= "abab", "abab"
    print(obj.buddyStrings(A, B))