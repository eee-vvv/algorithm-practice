def lengthOfLongestSubstring(self, s: str) -> int:
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
