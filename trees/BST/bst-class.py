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

bst = BST(5)

for i in [4,6,3,0,8,2,1,9,7]:
    if i != 5:
        bst.insert(i)

print('\n*******\n')
bst.in_order_map(print)
print('\n*******\n')
bst.pre_order_map(print)
print('\n*******\n')
bst.post_order_map(print)
print('\n*******\n')