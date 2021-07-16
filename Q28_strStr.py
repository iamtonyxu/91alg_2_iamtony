'''
实现strStr()函数。

给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def strStr(haystack: str, needle: str) -> int:
    if len(haystack) == 0 or len(needle) == 0:
        return 0
    i, j, start = 0, 0, 0
    while True:
        if i == len(haystack) or j == len(needle): break
        if needle[j] == haystack[i]:
            if j == 0: start = i
            j += 1
        else:
            if j != 0:
                i, j, start = start, 0, 0
        i += 1
    if j == len(needle): return start
    else: return -1

if __name__ == "__main__":

    haystack, needle = "hello", 'llo'
    print(strStr(haystack, needle))

    haystack, needle = "hello", ''
    print(strStr(haystack, needle))

    haystack, needle = 'a', 'a'
    print(strStr(haystack, needle))

    haystack, needle = 'a', 'ba'
    print(strStr(haystack, needle))

    haystack, needle = "mississippi", "issip"
    print(strStr(haystack, needle))