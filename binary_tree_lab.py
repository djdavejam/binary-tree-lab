from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Calculate the maximum depth (height) of a binary tree.
    
    The depth is the number of nodes along the longest path from the root 
    node down to the farthest leaf node. An empty tree has depth 0.
    
    Args:
        root: The root node of the binary tree (can be None)
    
    Returns:
        int: The maximum depth of the tree
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    """
    # Base case: if root is None (empty tree), depth is 0
    if root is None:
        return 0
    
    # Recursively calculate depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Return the maximum of the two depths plus 1 (for current node)
    return max(left_depth, right_depth) + 1

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor (LCA) of two nodes in a Binary Search Tree.
    
    The LCA is defined as the deepest node that has both p and q as descendants
    (a node can be a descendant of itself). This implementation leverages the
    BST property where left subtree values < root < right subtree values.
    
    Args:
        root: The root node of the BST
        p: First target node
        q: Second target node
    
    Returns:
        TreeNode: The lowest common ancestor node
    
    Time Complexity: O(h) where h is the height of the tree
    Space Complexity: O(h) for recursion stack in worst case (O(1) for iterative)
    """
    # Base case: if root is None, return None (shouldn't happen in valid BST)
    if root is None:
        return None
    
    # If both p and q are smaller than root, LCA lies in left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both p and q are greater than root, LCA lies in right subtree
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # If p and q are on different sides of root, or one equals root,
    # then root is the LCA
    else:
        return root