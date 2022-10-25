"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

## neetcode's O(1)
def productExceptSelf_n(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res

##O(1) space
def productExceptSelf(nums: list[int]) -> list[int]:
    output = [1]
    for i in range(len(nums)-1):
        output.append(nums[i] * output[i])
    for i in range(len(nums)-2,-1,-1):
        output[i] *= nums[i+1]
        nums[i] *= nums[i+1]
    return output

## O(n) space
def productExceptSelf_2(nums: list[int]) -> list[int]:
    prefix = []
    postfix = [1] * len(nums)

    for i in range(len(nums)):
        multiplier_1 = 1 if not i else prefix[i-1]
        multiplier_2 = 1 if not i else nums[i-1]
        prefix.append(multiplier_1 * multiplier_2)

    for i in range(len(nums)-1,-1,-1):
        multiplier_1 = 1 if i == len(nums)-1 else postfix[i+1]
        multiplier_2 = 1 if i == len(nums)-1 else nums[i+1]
        postfix[i] = (multiplier_1 * multiplier_2)
    print(f'i:{i}, m1:{multiplier_1}, m2:{multiplier_2}, p:{postfix}')

    output = [prefix[i] * postfix[i] for i in range(len(nums))]
    return output