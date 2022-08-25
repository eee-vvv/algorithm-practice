def best_sum(targ, nums, memo = {}):
    
    if targ in memo:
        return memo[targ]
    # base cases:
    if targ == 0:
        return []
    # targ < 0: clear history
    if targ < 0:
        return None
    
    best = None
    # recursive case:
    # loop through nums
    for n in nums:
        if n == 0:
            continue
        new_targ = targ - n
        new_result = best_sum(new_targ, nums)
        if new_result != None and (best == None or len(best) > len(new_result)):
            best = new_result + [n]
                
    # subtract num from targ (and add it to history)
    # call how sum on new targ and history
    memo[targ] = best
    return best

nums = [2,5]
targ = 8
print (best_sum(targ, nums))