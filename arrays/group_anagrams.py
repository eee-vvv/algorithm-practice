from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:

    anagrams = defaultdict([])

    for s in strs:
        histogram = [0] * 26 # making a hash for how many of each letter appears in s

        for c in s:
            histogram[ord(c) - ord('a')] += 1

        anagram_hash = tuple(histogram)

        anagrams[anagram_hash].append(s)

    return anagrams.values()