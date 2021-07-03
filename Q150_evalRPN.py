'''
根据 逆波兰表示法，求表达式的值。
有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
Example-1.
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
Example-2.
输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
Example-3.
输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：
该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opCollection = ['+', '-', '*', '/']
        pos, result = 0, 0
        opStack = []
        while True:
            if pos == len(tokens) and len(opStack) == 1: break
            # check the top is operator and do the calculation
            if opStack and opStack[-1] in opCollection:
                # pop the operator
                operator = opStack.pop()
                # pop num1, num2
                num2, num1 = int(opStack.pop()), int(opStack.pop())
                # do the calculation depending on the operator
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                else:
                    result = int(num1 / num2)
                # push result
                #if pos < len(tokens):
                opStack.append(result)
            else:
                opStack.append(tokens[pos])
                pos += 1
        result = opStack.pop()
        return result


if __name__ == "__main__":
    obj = Solution()
    tokens = [["2", "1", "+"],
              ["2","1","+","3","*"],
              ["4","13","5","/","+"],
              ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
              ['18']]
    for token in tokens:
        print(obj.evalRPN(token))