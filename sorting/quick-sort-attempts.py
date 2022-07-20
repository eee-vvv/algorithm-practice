from statistics import median

def partition(l: int,r: int, lst: list) -> int:
    '''
    picks a pivot element in a list and partitions the list 
    such that values smaller or equal to the pivot are to the left of the partition 
    and values greater than or equal to the pivot are to the right of the partiton
    '''
    print(f'l={l},r={r}')
    pivot = lst[(l+r)//2]
    p1, p2 = l, r
    while p1 < p2:
        if lst[p1] >= pivot:
            if lst[p2] <= pivot:
                lst[p1], lst[p2] = lst[p2], lst[p1]
                p1 += 1
            p2 -= 1
        else:
            p1 += 1
    print('pivot:',pivot)
    if pivot == lst[p2]:
        p2 -= 1
    return p2

# prt_lst = [3,4]
# assert(partition(0,1,prt_lst)== 0)
# assert(prt_lst == [3,4])

def quick_sort(l, r, lst:list)->list:
    if r <= l:
        return lst
    # if r <= l+1:
    #     if lst[r] < lst[l]:
    #         lst[r],lst[l] = lst[l],lst[r]
    #     return lst
    prt = partition(l,r,lst)
    print(lst, 'partition:',prt)
    quick_sort(l, prt-1, lst)
    print('right')
    quick_sort(prt,r, lst)
    return lst

srt_lst = [0,10,32,0,9]
print(srt_lst)
print(quick_sort(0,len(srt_lst)-1, srt_lst))

#problem = when we pick the right most element as the pivot and it's uniquely the largest

# def quick_sort(lst:list)->list:
#     length = len(lst)
#     if length <= 1:
#         return lst
#     #choose a pivot:
#     pivot = median([lst[0],lst[length//2],lst[-1]])
#     p1 = 0
#     p2 = length - 1
#     while p1 <= p2:
#         temp = None
#         if lst[p1] > pivot:
#             if lst[p2] < pivot:
#                 temp = lst[p1]
#                 lst[p1] = lst[p2]
#                 lst[p2] = temp
#                 p1 += 1
#             p2 -= 1
#         elif lst[p2] < pivot:
#             if lst[p1] >= pivot:
#                 temp = lst[p2]
#                 lst[p2] = lst[p1]
#                 lst[p1] = temp
#                 p2 -= 1
#             p1 +=1
#         else:
#             p1 += 1
#             p2 -= 1
#     return quick_sort(lst[:p2+1]) + quick_sort(lst[p1:])
#print(quick_sort([2,1,7,0]))