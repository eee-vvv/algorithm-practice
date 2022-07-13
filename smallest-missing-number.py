# find min missing num in a list of nums
# if no missing nums output nums[-1]+1
# In: [1, 2, 3], Out: 4
# In: [1, 3], Out: 2
# In: [4, 3, 1, 4], Out: 2
# In: [4, 2, 3], Out: 1
# In: [5, 3, 1], Out: 2

def smallest_missing_num_1(nums: list) -> int:
    length = len(nums)
    lowest = 0
    idx_of_lowest = 0
    # loop through nums
    for i in range(length):
        gap = True
        #loop through idx to the end of nums
        for j in range(i,length):
            #check inner idx agaist lowest
            if nums[j] == lowest + 1:
                lowest += 1
                gap = False
                idx_of_lowest = j
        if gap:
            return lowest + 1
        nums[idx_of_lowest] = nums[i]
        
        #if you never end up running into a case where we run into lowest + 1
            #return lowest + 1
        #if it's lowest + 1 then we switch it with the number at idx
    return lowest + 1

def smallest_missing_num(nums: list)-> int:
    # turn nums into keys of dict
    num_table = {}
    for n in nums:
        num_table[n] = True
    i = 1
    while i in num_table:
        i += 1
    return i
    # itterate through the natural nums and when you get to a key in dict that's missing, return that natural num
    
    

assert(smallest_missing_num([3,5,3,2]) == 1)
assert(smallest_missing_num([3,5,3,2,1]) == 4)
assert(smallest_missing_num([1]) == 2)

print(smallest_missing_num([3,5,3,2]) == 1, 
      smallest_missing_num([3,5,3,2,1]) == 4,
      smallest_missing_num([1]) == 2)