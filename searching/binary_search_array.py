def binary_search(targ: int, arr: list, start, end) -> int:
    current = (end + start) // 2
    if arr[current] == targ:
        return current
    if start >= end:
        return -1
    if arr[current] > targ:
        return binary_search(targ, arr, start, current - 1)
    if arr[current] < targ:
        return binary_search(targ, arr, current + 1, end)

# TESTS

print (binary_search(50, [0,1,2,3,4,5,6], 0, 6))
print (binary_search(8, [1,2,3,4,5,6,7,8], 0, 7))
print (binary_search(1, [1,2,3,4,5,6,7,8], 0, 7))
print (binary_search(2, [1,2,3,4,5,6,7,8], 0, 7))
print (binary_search(0, [0], 0, 0))
print (binary_search(1, [0], 0, 0))
