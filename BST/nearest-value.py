# given a tree and a target 
# return the value in your tree that's closest to the target

def findClosestValueInBst(tree, target):
    diff = tree.value - target 

    if tree.value == target:
        return target
    
    if diff > 0: # current val is bigger than target
        # base case:
        if tree.left == None:
            return tree.value
        #recursive:
        left_tree_closest = findClosestValueInBst(tree.left, target) # find the closest value in the left tree
        return tree.value if diff < abs(left_tree_closest - target) else left_tree_closest #compare it to the current node and return whichever is closer

    if diff < 0: # current val is smaller than target
        # base case:    
        if tree.right == None:
            return tree.value
        #recursive:
        right_tree_closest = findClosestValueInBst(tree.right, target) # find the closest value in the left tree
        return tree.value if abs(diff) < abs(right_tree_closest - target) else right_tree_closest #compare it to the current node and return whichever is closer
        #return your value or previous return value depending on which is closer to target

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None