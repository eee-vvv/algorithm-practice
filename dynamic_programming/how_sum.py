def how_sum(targ, nums, memo = {0 : []}):
    # base cases:
    if targ in memo:
        return memo[targ]
    # targ < 0: clear history
    if targ < 0:
        return None
    # 
    # recursive case:
    # loop through nums
    for n in nums:
        new_targ = targ - n
        new_result = how_sum(new_targ, nums, memo)
        if new_result != None:
            memo[targ] = new_result + [n]
            return memo[targ]
    # subtract num from targ (and add it to history)
    # call how sum on new targ and history
    memo[targ] = None
    return None

nums = [5,3,4,7]
targ = 7
print (how_sum(targ, nums))