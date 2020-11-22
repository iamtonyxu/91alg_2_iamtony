from collections import Counter
from typing import List

class Solution:
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # 1. 利用dict的子类Counter统计元素出现的次数，并返回出现频次前K高的元素
    c, res = Counter(nums), []
    for item in c.most_common(k):
        res.append(item[0])
    return res
