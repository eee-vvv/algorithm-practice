class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def in_order_map(self, func):
        if self.left:
            self.left.in_order_map(func)
        func(self.value)
        if self.right:
            self.right.in_order_map(func)
        return self
    
    def pre_order_map(self, func):
        func(self.value)
        if self.left:
            self.left.pre_order_map(func)
        if self.right:
            self.right.pre_order_map(func)
        return self
    
    def post_order_map(self, func):
        if self.left:
            self.left.post_order_map(func)
        if self.right:
            self.right.post_order_map(func)
        func(self.value)
        return self

    def insert(self, value):
        if value >= self.value:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        if value == self.value:
            return True
        if self == None:
            return False
        if value > self.value:
            return self.right.contains(value)
        if value < self.value:
            return self.left.contains(value)
        

    def remove(self, value):
        pass
        # if self == value
            # if has no right children:
                # return right child
            # if no left children:
                #return left child
        
        # set current value to self.value
        # set parent to none
        # while current value != value:
                # parent = current
            #if current value >=
                # assert current.right != None
                # current = current.right
            #if current vlaue <
                # assert current.left != None
                # current = current.left
                # base
        # no children
        # no right yes left
        # yes right no left
        # 
        return self
    
    def _depth_arr(self, depth, arr = []):
        l_max_d, r_max_d = (0,0)
        only_right = True if (self.right and not self.left) else False
        only_left = True if (self.left and not self.right) else False
        
        if only_right:
            self.left = BST(' ')
        if only_left:
            self.right = BST(' ')
            
        if self.left:    
            _, l_max_d = self.left._depth_arr(depth + 1, arr)
            
        arr.append((self.value, depth))
        
        if self.right:
            _, r_max_d = self.right._depth_arr(depth + 1, arr)
            
        return arr, max([l_max_d, r_max_d, depth])
        
    
    def visualize(self):
        d_arr, d = self._depth_arr(0)
        for i in range(d+1):
            s = ''
            for node in d_arr:
                if node[1] == i:
                    s += str(node[0])
                else:
                    s += ' '
            print(s)
                    
            
        
        # [ , ,1, , ]
        # [ ,/, ,\, ,]
        # [ ,2, ,3, ]
        # [/, ,\, , /, ,\, , , ]
        # [4/2\56/3\7]
        # [1,/,\,2,3,/,\,/,\,4,5,6,7]
        # 2**2 + 3(2**1) + 3(2**0)
        # 
        # 
        # [[[ ], ,[ ]],1,[[ ], ,[ ]]]
        # [[[ ],2,[ ]], ,[[ ],3,[ ]]]
        # [[[4], ,[3]], ,[[5], ,[6]]]
        # process in order
        # build array with (value, depth)
        # itterate through array depth times
        # printing val if element[depth] == depth, else ' ' for each element
        
        pass
    def _spaces_from_deapth(self,d):
        total = 2 ** d
        while d >= 0:
            total += 3 * (2 ** d)
            d -= 1
        return total

bst = BST(5)

for i in [1,8,6,7,0,2,6,9,10,2,0,14,70,20,11,22,71,69, -0, -2, -4,-3, -1]:
    bst.insert(i)

bst.visualize()

# print(bst._depth_arr(0)[0])
# print(bst._depth_arr(0)[1])

# print('\n*******\n')
# bst.in_order_map(print)
# print('\n*******\n')
# bst.pre_order_map(print)
# print('\n*******\n')
# bst.post_order_map(print)
# print('\n*******\n')