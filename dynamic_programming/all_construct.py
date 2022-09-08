def _all_construct(targ: str, parts: list[str], memo = {}) -> list[list[str]]:
    
    combos = []
    
    if targ == '':
        return combos + [[]]
    
    if targ in memo:
        return memo[targ]
    
    
    for part in parts:
        try:
            if targ.index(part) == 0:
                new_targ = targ[len(part):]   
                new_combos = _all_construct(new_targ, parts, memo)
                targ_combos = [[part] + nc for nc in new_combos]
                combos += targ_combos
        except:
            continue
   
    memo[targ] = combos
    return combos

def all_construct(targ, parts):
    return _all_construct(targ, parts, {})


print (all_construct('abcd', ['ab','c','d','abc'])) # [['ab', 'c', 'd'], ['abc', 'd']]
print (all_construct('abcd', ['c','abc'])) # []
print (all_construct('', ['ab','c','d','abc'])) # [[]]
print (all_construct('abc', ['ab'])) # []
print (all_construct('abc', ['abc'])) # [['abc']]
print (all_construct('12345', ['1','2','3','4','5','12','23','34','45','123','234','345','1234','2345','12345']))
#print (all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeee', ['e', 'ee', 'eee', 'efg']))