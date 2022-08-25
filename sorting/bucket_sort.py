
def bucket_sort(arr: list) -> list:
    ## find array min and max
    a_min = arr[0]
    a_max = arr[0]
    for num in arr:
        if num > a_max:
            a_max = num
        if num < a_min:
            a_min = num
    ## create a hash table of buckets from min-max w values initialized to 0
    buckets = {}
    for i in range(a_min,a_max+1):
        buckets[i] = None
    ## put the arr values into lists in their corrosponding hash table slots
    ## if they're doubles, append them to the preexisting list
    for num in arr:
        if buckets[num] != None:
            buckets[num].append(num)
        else:
            buckets[num] = [num]
    ## go through hash table keys in order
    ## add the values to a sorted list var if they're not Null
    sorted_arr = []
    for i in range(a_min,a_max+1):
        if buckets[i] != None:
            for j in buckets[i]:
                sorted_arr.append(j)
    return sorted_arr
