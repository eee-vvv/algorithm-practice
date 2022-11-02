'''
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output 
and the order of the triplets does not matter.
'''

def threeSum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    res = []
    for i,n in enumerate(nums):
        if i >= 1 and n == nums[i-1]:
            continue
        l,r = i + 1, len(nums) - 1
        while l < r:
            sum3 = n + nums[r] + nums[l]
            if sum3 > 0:
                r -= 1
            if sum3 < 0:
                l += 1
            if not sum3:
                res.append([n,nums[l],nums[r]])
                l += 1 
                while nums[l] == nums[l-1] and l < r:
                    l+=1
    return res


