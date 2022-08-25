import math
def order_mag(num):
    order = 0
    while num >= 10:
        num = num/10
        order += 1
    return order


def radix_sort(arr: list, radix = 10)-> list:
    #find the order of magnitude of the biggest number in arr
    a_max = max(arr)
    order = order_mag(a_max)
    sorted_arr = arr
    #for every order of magnitude (starting at 0) in our max number...
    for o in range(order + 1):
        #initialize bucket hash table with radix num buckets
        buckets = {i:None for i in range(radix)}
        for num in sorted_arr:
            #get num's digit corrosponding to our order of magnitude
            sort_digit = math.trunc((num / (10 ** o)) % 10)
            #num in the bucket for that digit
            #if there's nums alread in the bucket, append num to their list
            if buckets[sort_digit] != None:
                buckets[sort_digit].append(num)
            else:
                buckets[sort_digit] = [num]
        #clear our sorted array to prepare for this itteration
        sorted_arr = []
        #pour our buckets in order, into our sorted array
        #with every order of magnitude, 
        #the relative order with respect to previous magnitudes is preserved        
        for i in range(radix):
            if buckets[i] != None:
                for j in buckets[i]:
                    sorted_arr.append(j)
        print(sorted_arr)
    return sorted_arr
