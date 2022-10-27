'''
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
'''

def longestConsecutive(nums: list[int]) -> int:
    nums_s = set(nums)
    longest = 0

    for n in nums:
        counter = 0
        if (n - 1) not in nums_s: #this is the start of a consecutive series
            while (n + counter) in nums_s: #check how long that series is
                counter += 1
            longest = max(counter, longest)
            
    return longest