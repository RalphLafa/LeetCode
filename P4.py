from typing import List

a = [1, 3]
b = [2]

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums3 = nums1 + nums2
    nums3.sort()
    n = len(nums3)
    if n%2 == 1:
        return nums3[int(n/2)]
    else:
        return (nums3[n//2-1] + nums3[n//2])/2
    
c = findMedianSortedArrays(a,b)
print(c)