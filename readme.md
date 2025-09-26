# Binary Tree Lab - Depth and Ancestors

A Python implementation of two classic binary tree algorithms.

## 🎯 What This Lab Does

This lab implements two essential binary tree functions:

1. **Maximum Depth** - Find the deepest path from root to leaf
2. **Lowest Common Ancestor** - Find the shared ancestor of two nodes in a BST

## 🚀 Quick Start

### Run the Tests
```bash
python binary_tree_tests.py
```

### Project Structure
```
binary-tree-lab/
├── binary_tree_lab.py    # Main implementation
├── binary_tree_tests.py  # Test suite
└── README.md            # This file
```

## 💡 Functions Implemented

### `max_depth(root)`
- **Purpose**: Calculate maximum depth of a binary tree
- **Input**: Root node of tree (or None for empty tree)
- **Output**: Integer depth (0 for empty tree)
- **Algorithm**: Recursive traversal

### `lowest_common_ancestor(root, p, q)`
- **Purpose**: Find lowest common ancestor in a Binary Search Tree
- **Input**: Root node and two target nodes
- **Output**: The ancestor node
- **Algorithm**: BST property-based traversal

## ✅ Test Results
All tests pass:
- Max depth: Empty, single node, balanced, and skewed trees
- LCA: Standard cases, deep nodes, and ancestor relationships

## 🔧 How It Works

**Max Depth Algorithm:**
1. If tree is empty → return 0
2. Calculate left subtree depth
3. Calculate right subtree depth  
4. Return max(left, right) + 1

**LCA Algorithm:**
1. If both nodes < current → go left
2. If both nodes > current → go right
3. Otherwise → current node is LCA

## 📚 Time Complexity
- **Max Depth**: O(n) - visits each node once
- **LCA**: O(h) - follows one path down tree

*Where n = number of nodes, h = height of tree*