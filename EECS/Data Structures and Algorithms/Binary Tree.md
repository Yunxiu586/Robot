# Binary Tree

A **binary tree** is a hierarchical data structure in which each node has at most two children, referred to as the **left child** and **right child**. 

+ **Root**: The topmost node (no parent).
+ **Parent/Child**: A node directly above/below another.
+ **Leaf**: A node with no children.
+ **Internal Node**: A node with at least one child.
+ **Depth**: The number of edges from the root to a node.
+ **Height**: The number of edges on the longest path from a node to a leaf. The height of the tree is the height of the root.
+ **Subtree**: A tree consisting of a node and all its descendants.



##### Binary Search Tree (BST)

For any node, all keys in its left subtree are less than its key, and all keys in its right subtree are greater.

**Search**

+ Start at the root. Compare the target key with the current node's key.
  + If equal, **Found**.
  + If target is smaller, recurse/iterate into the **left** subtree.
  + If target is larger, recurse/iterate into the **right** subtree.
  + If a `null` subtree is reached, **Not found**.
+ Complexity : $\text O(\log n)$

**Insertion**

+ Perform a **search** for the key until reaching a `null`subtree. At that point, create a new node and attach it as the left or right child of the last visited node.
+ Insertions always occur at a new **leaf** position.
+ Complexity : $\text O(\log n)$

**Construction**

+ Start with an empty tree. **Iteratively insert** each key from the sequence using the insertion algorithm.
+ The structure (and thus height `h`) of the resulting BST depends on **the insertion order**. Inserting a sorted sequence yields a linked list with height $\text O(n)$. For optimal balance, the median of the set should  ideally be the root.

**Delete**

+ Leaf : Remove the node.

+ One child : Remove the node and promote its single child to take its place.

+ Two children :

  + Find the node's **in-order successor** (smallest node in its right subtree) or **in-order predecessor** (largest node in its left subtree).

  + Copy the successor's (or predecessor's) key into the target node.

  + Recursively delete that successor/predecessor node.