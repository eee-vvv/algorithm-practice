#def merge(arr, start_a, end_a):
    

def merge_sort(lst: list) -> list:
    
    length = len(lst)
    
    if length <= 1:
        return lst
    
    sub_1 = merge_sort(lst[:length//2])
    sub_2 = merge_sort(lst[length//2:])
    idx_1 = 0
    idx_2 = 0
    sorted_lst = []

    while idx_1 < len(sub_1) and idx_2 < len(sub_2):
        if sub_1[idx_1] < sub_2[idx_2]:
            sorted_lst.append(sub_1[idx_1])
            idx_1 += 1
        else:
            sorted_lst.append(sub_2[idx_2])
            idx_2 += 1
    if idx_1 < len(sub_1):
        sorted_lst += (sub_1[idx_1:])
    else:
        sorted_lst += (sub_2[idx_2:])
    return sorted_lst