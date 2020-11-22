class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 遍历字串，将每个不含重复字符的子串长度记录在数组，然后返回数组的最大值
        # 注意：1.如果查找字符包含在工作子串，先记录工作子串的长度，然后查找字符在工作子串的位置，以此更新工作子串
        # 注意：2.最后一组工作子串的长度需要额外添加到数组
        strArray, tmp = [], []
        for c in s:
            if c in tmp:
                strArray.append(len(tmp))
                tmp = tmp[tmp.index(c)+1:] + [c]
            else:
                tmp.append(c)
        strArray.append(len(tmp))
        strArray.sort()
        return strArray[-1]