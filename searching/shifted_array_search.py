# [1,2,3,4,5]

def find_pivot(shiftArr):
  begin = 0
  end = len(shiftArr) - 1
  while begin <= end:
    mid = (begin + end) // 2
    if shiftArr[mid] < shiftArr[mid - 1]:
      return mid
    if shiftArr[mid] > shiftArr[0]:
      begin = mid + 1
    else:
      end = mid - 1
  return 0
        
def binary_search(arr, num, begin, end):
  while begin <= end:
    mid = (begin + end) // 2
    if arr[mid] == num:
      return mid 
    if arr[mid] > num:
      end = mid - 1
    else:
      begin = mid + 1
  return -1

def shifted_arr_search(shiftArr, num):
  pivot = find_pivot(shiftArr)
  # now we essentially have two sorted arrays
  if (pivot == 0 or num < shiftArr[0]): # then num must appear after pivot
    return binary_search(shiftArr, num, pivot, len(shiftArr) -1)
  # if num apprears before pivot
  return binary_search(shiftArr, num, 0, pivot -1)

#TESTS

print(shifted_arr_search([6,7,1,2,3,4,5], 1)) #2
print(shifted_arr_search([6,7,1,2,3,4,5], 7)) #1
print(shifted_arr_search([6,7,1,2,3,4,5], 4)) #5
print(shifted_arr_search([6,7,1,2,3,4,5], 0)) #-1
print(shifted_arr_search([1,2,3,4,5], 4)) #3
print(shifted_arr_search([1], 1)) #0
print(shifted_arr_search([1], 2)) #-1
print(shifted_arr_search([2,3], 1)) #-1

# function shiftedArrSearch(shiftArr, num):
#     pivot = findPivotPoint(shiftArr)

#     if(pivot == 0 OR num < shiftArr[0]):
#         return binarySearch(shiftArr, pivot, shiftArr.length - 1, num)
    
#     return binarySearch(shiftArr, 0, pivot - 1, num)


# function findPivotPoint(arr):
#     begin = 0
#     end = arr.length - 1

#     while (begin <= end):
#         mid = begin + floor((end - begin)/2)
#         if (mid == 0 OR arr[mid] < arr[mid-1]): ## we found it
#             return mid
#         if (arr[mid] > arr[0]): ## everything up to mid is in order
#             begin = mid + 1 ## the pivot is somewhere after mid
#         else:
#             end = mid - 1 ## the pivot must be somewhere before mid

#     return 0

# # [6,7,1,2,3,4,5]


# function binarySearch(arr, begin, end, num):
#     while (begin <= end):
#         mid = begin + floor((end - begin)/2)
#         if (arr[mid] < num):
#             begin = mid + 1
#         else if (arr[mid] == num):
#             return mid
#         else:
#             end = mid - 1

#     return -1