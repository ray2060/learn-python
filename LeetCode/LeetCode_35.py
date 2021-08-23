class Solution:
    def sort(self, ls):
        for i in range(len(ls) - 1):
            minj = i
            for j in range(i + 1, len(ls)):
                if ls[j] < ls[minj]:
                    minj = j
                if i == minj:
                    continue
                ls[i], ls[minj] = ls[minj], ls[i]
        return ls
    
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        nums.append(target)
        nums = self.sort(nums)
        return nums.index(target)
