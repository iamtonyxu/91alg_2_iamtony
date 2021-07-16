'''
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的输入。
E1
输入：s = "3[a]2[bc]"
输出："aaabcbc"
E2
输入：s = "3[a2[c]]"
输出："accaccacc"
E3
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
E4
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
'''

class Solution:
    '''
    def decodeString(self, s: str) -> str:
        index, decodeStack = 0, []
        while index < len(s):
            # push
            if s[index] == ']':
                decodeStack.append(']')
            elif s[index].isalnum():
                decodeStack.append(s[index])
            index += 1

            # pop, operation then push
            if decodeStack and decodeStack[-1] == ']':
                # discard ']'
                decodeStack.pop()
                # get encode_string, repeat_number and calculate decode_string
                decode_string = decodeStack.pop()
                while decodeStack and decodeStack[-1].isalpha():
                    decode_string = decodeStack.pop() + decode_string
                repeat_number, times = 0, 1
                while decodeStack and decodeStack[-1].isdigit():
                    repeat_number += (int)(decodeStack.pop()) * times
                    times *= 10
                decode_string = decode_string * repeat_number
                decodeStack.append(decode_string)

        # read decode_string from the stack
        result = ""
        for decode_str in decodeStack:
            result += decode_str
        return result
    '''

    def decodeString(self, s: str) -> str:
        index, decodeStack = 0, []
        while index < len(s):
            # push
            decodeStack.append(s[index])
            index += 1

            # pop -> decode -> push
            if decodeStack and decodeStack[-1] == ']':
                decodeStack.pop() # discard ']'
                # get enc_str, repeats and calculate dec_str
                enc_str = decodeStack.pop()
                while decodeStack and decodeStack[-1].isalpha():
                    enc_str = decodeStack.pop() + enc_str
                decodeStack.pop() # discard '['
                repeats, times = 0, 1
                while decodeStack and decodeStack[-1].isdigit():
                    repeats += (int)(decodeStack.pop()) * times
                    times *= 10
                dec_str = enc_str * repeats
                decodeStack.append(dec_str)

        #read result from decodeStack
        result = ""
        for dec_str in decodeStack:
            result += dec_str
        return result



if __name__ == "__main__":
    obj = Solution()
    input = ["2[a]2[bc]", "3[a2[c]]", "2[abc]13[cd]ef", "abc3[cd]xyz"]
    for encoded_str in input:
        decoded_str = obj.decodeString(encoded_str)
        print(decoded_str)