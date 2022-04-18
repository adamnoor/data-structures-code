class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        track = {}
        smallest_positive = None
        for i in range(0, len(nums)):
            if nums[i] > 0:
                if smallest_positive is None:
                    smallest_positive = nums[i]
                elif nums[i] < smallest_positive:
                    smallest_positive = nums[i]
                if nums[i] not in track:
                    track[nums[i]] = True
                else:
                    pass
        
        if smallest_positive == None:
            return 1
        elif smallest_positive == 2:
            return 1
        else:
            for i in range(1, 2**31-1):
                if i not in track:
                    return i
