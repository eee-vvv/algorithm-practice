class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        for i in range(len(array), -1,-1):
            self.siftDown(i, array)
        return array

    def siftDown(self, idx, h):
        # take the root node and keep swapping her with 
        # the smallest of her child nodes
        length = len(h)
        while True:
            # print(f'idx:{idx}, h:{h}')
            c1_idx = (idx * 2) + 1
            c2_idx = c1_idx + 1
            c_by_size = []
            if c1_idx >= length: # no children left
                break
            c_by_size = [(c1_idx, h[c1_idx])]
            if c2_idx < length:
                c_by_size.append((c2_idx,h[c2_idx]))
            c_by_size.sort(key = lambda c: c[1])
            # print(f'children: {c_by_size}')
            # print(f'first child[1]:{c_by_size[0][1]}')
            # print('\n')
            if h[idx] <= c_by_size[0][1]:
                break
            h[idx], h[c_by_size[0][0]] = h[c_by_size[0][0]], h[idx]
            idx = c_by_size[0][0]
                

        

    def siftUp(self):
        # take the leaf-iest node and keep swapping w her parent
        # untill parent is smaller or no parent
        idx = len(self.heap) - 1
        while True:
            par_idx = (idx - 1)//2
            if par_idx < 0 or self.heap[idx] > self.heap[par_idx]:
                break
            self.heap[idx], self.heap[par_idx] = self.heap[par_idx], self.heap[idx]
            idx = par_idx


    def peek(self):
        return self.heap[0] 

    def remove(self):
        h = self.heap
        h[0],h[-1] = h[-1],h[0]
        removed = h.pop()
        self.siftDown(0,h)
        return removed
        

    def insert(self, value):
        h = self.heap
        h.append(value)
        self.siftUp()