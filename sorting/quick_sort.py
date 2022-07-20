def partition(l,r,arr):
    pivot = arr[len(arr)//2]
    l -= 1
    r += 1
    while True:
        l += 1
        while arr[l] < pivot:
            l += 1
        r -= 1
        while arr[r] > pivot:
            r -= 1
        if l > r:
            return l
        arr[l], arr[r] = arr[r], arr[l]

def quick_sort_inner(l,r,arr):
    p = partition(l,r,arr)
    partition(l,p-1,arr)
    partition(p,r,arr)
    return arr

def quick_sort(arr):
    return quick_sort_inner(0,len(arr)-1,arr)


# 5
# 4 8 2 7 5
# 4 5 2 7 8
# 4 5 2 7 8

