'''
请你设计一个支持下述操作的栈。
实现自定义栈类 CustomStack：

CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量，栈在增长到 maxSize 之后则不支持 push 操作。
void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
int pop()：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 -1 。
void inc(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。
'''

class CustomStack:

    def __init__(self, maxSize: int):
        self.cur, self.total = 0, maxSize
        self.data = []

    def push(self, x: int) -> None:
        if self.cur < self.total:
            self.data.append(x)
            self.cur += 1

    def pop(self) -> int:
        if self.cur > 0:
            self.cur -= 1
            return self.data.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if self.cur > k:
            for i in range(k):
                self.data[i] += val
        else:
            for i in range(self.cur):
                self.data[i] += val


if __name__ == "__main__":
# Your CustomStack object will be instantiated and called as such:
maxSize, k, val = 3, 2, 100
obj = CustomStack(maxSize)
obj.push(1)
obj.push(2)
param_2 = obj.pop()
obj.increment(k, val)
print(obj.data)