class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Constructing the BST manually:
#       10
#      /  \
#     5    15
#    / \   / \
#   2   5 13  22

root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(2)
root.left.right = BSTNode(5)
root.right.left = BSTNode(13)
root.right.right = BSTNode(22)



def findClosestValueInBST(tree, target):
    return findClosestHelper(tree, target, float("inf"))

def findClosestHelper(node, target, closest):
    # Traverse the tree
    current_node = node
    while current_node is not None:
        # Update closest if the current node is closer to the target
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        # Move left or right based on the target value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break  # If the target equals current node's value, it's the closest possible
    return closest



target = 12
print(findClosestValueInBST(root, target))