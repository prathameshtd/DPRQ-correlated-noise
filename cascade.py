import numpy as np

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_tree(k, sd):
    def create_node(k, value):
        if k == 0:
            left_node = None
            right_node = None
            return Node(value, left_node, right_node)
        else:
            #Y = np.random.standard_normal()
            Y = np.random.normal(0, sd)
            left_value = value / 2 + np.sqrt(3) / 2 * Y
            right_value = value / 2 - np.sqrt(3) / 2 * Y
            left_node = create_node(k - 1, left_value)
            right_node = create_node(k - 1, right_value)
            return Node(value, left_node, right_node)

    #root_value = np.random.standard_normal()
    root_value = np.random.normal(0, sd)
    return create_node(k, root_value)


def print_leaf_nodes(node):
    if node:
        # If this node is a leaf node, print its value
        if not node.left and not node.right:
            print(node.value)
        else:
            # Otherwise, recurse on the children
            print_leaf_nodes(node.left)
            print_leaf_nodes(node.right)

def get_leaf_values(node):
    leaf_values = []

    def traverse(node):
        if node:
            # If this node is a leaf node, store its value
            if not node.left and not node.right:
                leaf_values.append(node.value)
            else:
                # Otherwise, recurse on the children
                traverse(node.left)
                traverse(node.right)
    
    traverse(node)

    return np.array(leaf_values)