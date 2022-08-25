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

minimum_bribes([1,2,5,3,7,8,6,4])

1 2 3 4 5 6 7 8
1 2 3 5 4 6 7 8
1 2 5 3 4 6 7 8
1 2 5 3 4 7 6 8
1 2 5 3 7 4 6 8
1 2 5 3 7 4 8 6 


2
2
1


1
2
4