"""
    Given an integer array nums and an integer k, 
    return the k most frequent elements. 
    You may return the answer in any order.
"""
## Using Bucket Sort
def topKFrequent_bs(nums: list[int], k: int) -> list[int]:

        hist = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hist[n] = 1 + hist.get(n,0)
        for n, c in hist.items():
            buckets[c].append(n)

        output = []

        for i in range(len(buckets) - 1, 0, -1):
            output.extend(buckets[i])
            if len(output) >= k:
                return output

## Using a Heap
def topKFrequent_h(nums: list[int], k: int) -> list[int]:
    

        # output = []
        # hist = defaultdict(int)
        # for n in nums:
        #     hist[n] += 1
        # sorted_count = sorted(list(hist.values()))
        # all_nums = set(nums)
        # for i in range(k):
        #     count = sorted_count.pop()
        #     for n in hist.keys():
        #         if hist[n] == count and n in all_nums:
        #             output.append(n)
        #             all_nums.remove(n)
        # return output