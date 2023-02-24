def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        first = 0
        last = 0
        for i in range(len(nums)):
            if target == nums[i]:
                result.append(i)

        if len(result) == 0:
            first, last = -1, -1
        else: 
            first, last = result[0], result[-1]
            
        result = [first, last]

        return result