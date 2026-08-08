class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0) +1
        bucket = [[] for _ in range(len(nums)+1)]
        for n, f in counter.items():
            bucket[f].append(n)
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return result        