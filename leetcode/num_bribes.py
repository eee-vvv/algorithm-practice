### Solution 1
def minimum_bribes(q):
    bribes = 0

    for i, o in enumerate(q):
        cur = i + 1

        if o - cur > 2:
            print("Too chaotic")
            return
        
        weird_lst = q[max(o - 2, 0):i]
        for k in weird_lst:
            if k > o:
                bribes += 1

    print(bribes)

### Solution 2
def minimumBribes(q):
    bribes = 0
    needs_swaps = True
    length = len(q)
    # loop through array backwards while there's an instance of an element != its index + 1
    while needs_swaps:
        needs_swaps = False
        for i in range(length - 1, -1,-1):
            if q[i] - i > 3: # if element - index > 3 print too chaotic and return
                print ('Too chaotic')
                return
            if i + 1 < length:
                if q[i] > q[i+1]: # if element > element at i + 1 then swap the two and increment swaps
                    bribes += 1
                    needs_swaps = True
                    q[i],q[i+1] = q[i+1], q[i]
    print (bribes)



minimum_bribes([1,2,5,3,7,8,6,4])