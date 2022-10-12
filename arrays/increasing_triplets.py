# Given an integer array nums, 
# return true if there exists a triple of indices (i, j, k) 
# such that i < j < k and nums[i] < nums[j] < nums[k]. 
# If no such indices exists, return false.

def increasingTriplet(nums: list[int]) -> bool:
    s,m = (float('inf'),float('inf'))
    for n in nums:
        if n <= s:
            s = n
        elif n <= m:
            m = n
        else:
            return True
    return False