from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def i_dfs(self):
        stack = [self]
        arr = []
        while stack:
            current = stack.pop()
            arr.append(current.name)
            stack += (reversed(current.children))
        return arr
    
    def r_dfs(self,arr):
        arr.append(self.name)
        for c in self.children:
            c.r_dfs(arr)
        return arr
            
    
    # ### ITTERATIVE
    # def _processNode(self, output: list, q: list):
    #     output.append(q.pop(0).name)
    #     q = self.children + q
    #     return q, output

    # def i_depthFirstSearch(self):
    #     output = []
    #     q = [self]
    #     while q:
    #         self = q[0]
    #         q, output = self._processNode(output,q)
    #     return output
    
    # ### RECURSIVE
    # def depthFirstSearch(self, array: list):
    #     array.append(self.name)
    #     for c in self.children:
    #         c.depthFirstSearch(array)
    #     return array