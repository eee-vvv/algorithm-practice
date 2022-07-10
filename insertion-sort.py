def insertion_sort(lst: list) -> list:
    length = len(lst)
    for i in range(1,length):
        pointer = i - 1
        temp = lst[i]
        while lst[pointer] > temp and pointer >= 0:
            lst[pointer+1] = lst[pointer]
            pointer -= 1
        lst[pointer+1] = temp
    return lst


print(insertion_sort([2,1,100,3,6,4,7,9,2,0]))

# import random 
# import timeit

# for x in range(12):
#     t = timeit.timeit(f'insertion_sort([random.random() for x in range({x})])', globals=globals())
#     print(f'{x} {t:0.02}')