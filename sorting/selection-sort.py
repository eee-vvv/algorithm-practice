def selection_sort(lst: list) -> list:
    length = len(lst)
    # outer loop through list
    for i in range(length):
        idx_of_smallest = i
        # inner loop through rest of list saving "smallest so far" in temp var
        for j in range(i+1, length):
            if lst[idx_of_smallest] > lst[j]:
                idx_of_smallest = j
        # switch outerloop index value with "smallest so far."
        temp = lst[i]
        lst[i] = lst[idx_of_smallest]
        lst[idx_of_smallest] = temp
    return lst

print(selection_sort([2,1,100,3,6,4,7,9,2,0]))
    