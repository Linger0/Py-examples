import uuid
from graphviz import Digraph

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root
        self.dot = Digraph(comment='Tree', format='png')
    def printTree(self, savePath = 'Tree'):
        def printChildren(parent: TreeNode, parTag: str):
            if parent.left:
                lTag = str(uuid.uuid1())
                self.dot.node(lTag, str(parent.left.val))
                self.dot.edge(parTag, lTag)
                printChildren(parent.left, lTag)
            if parent.right:
                rTag = str(uuid.uuid1())
                self.dot.node(rTag, str(parent.right.val))
                self.dot.edge(parTag, rTag)
                printChildren(parent.right, rTag)
        if isinstance(self.root, TreeNode):
            rootTag = str(uuid.uuid1())
            self.dot.node(rootTag, str(self.root.val))
            printChildren(self.root, rootTag)
        self.dot.render(savePath)