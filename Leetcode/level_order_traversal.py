'''
implement the level orderl traversal of a binary tree 
with recursive method.
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(value_list):
    if not value_list:
        return 
    
    data = value_list.pop(0)
    if data:
        node = TreeNode(data)
        node.left = build_tree(value_list)
        node.right = build_tree(value_list)
        return node
    else:
        return 
    
    

def pre_order_traversal(node):
    if not node:
        return 
  
    print(node.val)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

result = {}
def level_order_traversal(node, level):
    global result
    if not node:
        return
    
    if level in result:
        result[level].append(node.val)
    else:
        result[level] = [node.val]
    
    level_order_traversal(node.left, level+1)
    level_order_traversal(node.right, level+1)

    return 
    

input_list = [1,2,4,None,None,5,None,None,3,None,6,None,None]
tree_root = build_tree(input_list)
pre_order_traversal(tree_root)
level_order_traversal(tree_root, 0)
print(result)