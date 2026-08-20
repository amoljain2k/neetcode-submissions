class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i,v in enumerate(nums):
            if v in window:
                return True
            window.add(v)
            if len(window)>k:
                window.remove(nums[i-k])
        return False
        