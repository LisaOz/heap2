# HEAP IMPLEMENTATION IN PYTHON

This Python script demonstrates a **Heap** class implementation for a min-heap data structure. 
A **Heap** is a tree-based data structure that satisfies the three heap properties:
1. Order Property
2. Balance Property
3. Complete Property

### Order Property:
- In a max-heap, for every node 'i' other than the root, the value of parent is greater than or equal to the value of children.
- In a min-heap, for every node 'i', other than the root, the value of parent is less than or equal to the value of its children.

### Balance Property:
- all leaves of the heap have depth that differ by at most one level.

### Complete Binary Tree Property:
- In a heap,  all levels of the tree, except possibly the last one (deepest), are fully filled.
If the last level is not complete, the nodes are filled from left to right.

## Class Heap

The **Heap** class provides methods to maintain and manipulate a min-heap, 
and contains the following methods:
- **def __init__(self)**: Class constructor
- **def insert(self, x)**: Adds a new element and ensures that the heap property is maintained by calling **sift_up**
- **def sift_up(self, i)**: Moves an element up the heap if it is smaller than its parent
- **def extract_min(self)**: Removes and returns the smallest element from the heap with **sift_down**
- **def sift_down(self, i)**: Moves an element down the heap if it is larger than its children
  

  
  
