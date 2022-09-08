def _count_construct(targ: str, parts: list[str], memo = {}) -> int:
    
    if targ == '':
        return 1
    
    if targ in memo:
        return memo[targ]
    
    ways = 0
    
    for part in parts:
        try:
            if targ.index(part) == 0:
                new_targ = targ[len(part):]
                new_ways = _count_construct(new_targ, parts, memo)
                ways += new_ways
        except:
            continue
        
    memo[targ] = ways
    return ways

def count_construct(targ, parts):
    return _count_construct(targ, parts, {})


print (count_construct('abcd', ['ab','c','d','abc'])) # 2
print (count_construct('abcd', ['c','abc'])) # 0
print (count_construct('', ['ab','c','d','abc'])) # 1
print (count_construct('abc', ['ab'])) # 0
print (count_construct('abc', ['abc'])) # 1
print (count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeee', ['e', 'ee', 'eee', 'efg'])) # 15902591