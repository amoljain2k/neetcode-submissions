class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t>temperatures[stack[-1]]:
                day = stack.pop()
                res[day] = i-day
            stack.append(i)
        return res
        