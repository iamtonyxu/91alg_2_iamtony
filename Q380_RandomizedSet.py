'''
设计一个支持在平均时间复杂度 O(1)下，执行以下操作的数据结构。

insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

示例：
// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.array = []
        self.n = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data: return False
        self.data[val] = self.n
        self.array.append(val)
        self.n += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data: return False
        # find index of val in the array
        index = self.data[val]
        # move the last item to the deleted one
        self.data[self.array[-1]] = index
        # delete val
        self.data.pop(val)
        # update self.array
        self.array[index] = self.array[-1]
        self.array.pop()
        self.n -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        #return self.array[random.randint(0, self.n-1)] # Wrong output
        return self.array[int(random.random() * self.n)] # Correct

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

obj = RandomizedSet()
for i in range(10):
    print(obj.insert(i))

print('obj.n = ', obj.n)

for i in range(20):
    print(obj.getRandom())


for i in range(10):
    print(obj.remove(i))

print('obj.n = ', obj.n)
