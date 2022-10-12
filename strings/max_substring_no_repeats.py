# Given a string s, 
# find the length of the longest substring 
# without repeating characters.



## better memory
def lengthOfLongestSubstring1(s: str) -> int:
    
    chars = set()
    l = 0
    mx = 0
    
    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        mx = max(mx, r - l + 1)
    
    return mx

## better runtime??
def lengthOfLongestSubstring2(s: str) -> int:
    
    seen = {} # c:i
    longest = 0
    start = 0
    
    for end, c in enumerate(s): # increment end as for loop
        if c in seen and seen[c] >= start: # if c at end in seen and i >= start
            start = seen[c] + 1 # move start to i + 1,
        seen[c] = end
        longest = end - start if end - start > longest else longest
        
    return min([longest + 1, len(s)])


def lengthOfLongestSubstring3(s: str) -> int:
    
    p1 = 0
    longest_substring = 0
    most_recent_idx = {}
    
    for i, c in enumerate(s):
        if c in most_recent_idx and most_recent_idx[c] >= p1:
            longest_substring = max([i - p1, longest_substring])
            p1 = most_recent_idx[c] + 1
            if i == len(s) - 1:
                p1 = i
            
        most_recent_idx[c] = i
    
    if p1 == 0:
        return len(s)
                
    return max([longest_substring, len(s) - p1])
