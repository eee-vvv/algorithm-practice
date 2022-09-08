def _can_construct(targ: str, parts: list[str], mem = {}):
    
    if targ in mem:
        return mem[targ]
    if targ == '':
        return True
    
    for part in parts:
        
        try:
            if targ.index(part) == 0: #ANKI
                new_targ = targ[len(part):]
                
                if _can_construct(new_targ, parts, mem):
                    mem[targ] = True
                    return True
                
        except:
            continue
        
    mem[targ] = False
    return False

def can_construct(targ, parts):
    return _can_construct(targ, parts, {})

print (can_construct('abcd', ['ab','c','d','abc'])) # True
print (can_construct('abcd', ['c','abc'])) # False
print (can_construct('', ['ab','c','d','abc'])) # True
print (can_construct('abc', ['ab'])) # False
print (can_construct('abc', ['abc'])) # True