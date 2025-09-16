# Data Structures
## Linear
### Arrays

### Hash Tables

### Linked Lists
- Collection of Nodes
- Nodes are pointed to the next node (singular) or next and previous (doubly linked list
- Adding and removing is typically faster
- no fixed size
- More memory
- searching is slow
- don't know how many items will be in the list
- don't need random access to elements
- Want to insert in the middle of the list
- Need constant time for addition and deletion

```python
class Node:    
	def __init__(self,value):        
		self.value = value        
		self.next = None
```

```python
class LinkedList:
	def __init__(self,head=None):
		self.head = head    
        def append(self, new_node):
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node
	def delete(self, value):
            """Delete the first node with a given value."""
            current = self.head
            if current.value == value:
                self.head = current.next
            else:
                while current:
                    if current.value == value:
                        break
                    prev = current
                    current = current.next
                if current == None:
                    return
                prev.next = current.next
                current = None
        def insert(self, new_element, position):
            """Insert a new node at the given position.
            Assume the first position is "1".
            Inserting at position 3 means between
            the 2nd and 3rd elements."""
            count=1
            current = self.head
            if position == 1:
                new_element.next = self.head
                self.head = new_element
            while current:
                if count+1 == position:
                    new_element.next =current.next
                    current.next = new_element
                    return
                else:
                    count+=1
                    current = current.next
                # break

            pass
	def print(self):
            current = self.head
            while current:
                print(current.value)
                current = current.next
```

### Stacks

### Queues

## Non-Linear

### Trees
- Trees are collection of Nodes 
- Nodes are connected via Edges
- Nodes contain data or a value
- Nodes may or may not have children

FreeCodeCamp terminology summary

- Root is the topmost node of the tree
- Edge is the link between two nodes
- Child is a node that has a parent node
- Parent is a node that has an edge to a child node
- Leaf is a node that does not have a child node in the tree
- Height is the length of the longest path to a leaf
- Depth is the length of the path to its root

#### Binary Trees
- Each node has at most two children
- left_child
- right_child
- and contains a value

Code example:

```python
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
```

Tree Traversal
- Depth-First Search (DFS)
- Breadth-First Search (BFS)

##### Binary Search Tree
- ordered or sorted binary trees
- keeps values sorted order
- Binary Search Node is larger than value of the offspring of its left child
- Binary Search Node is smaller than value of the offspring of its right child 

Coding Example:

```python
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

```

### Graphs

# Algorithms
## Depth-First Search (DFS)
- used in tree traversal
- requires going down to each leaf node before backtracking
### DFS Types
- pre-order
  ```python
    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()
  ```
- in-order
  ```python
    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()
  ```
- post-order
  ```python
    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value)
  ```
## Breadth-First Search (BFS)
- Used in tree traversal
- traverses the tree level by level and depth by depth

Code:

```python
def bfs(self):
    queue = Queue()
    queue.put(self)

    while not queue.empty():
        current_node = queue.get()
        print(current_node.value)

        if current_node.left_child:
            queue.put(current_node.left_child)

        if current_node.right_child:
            queue.put(current_node.right_child)
```

# Resources
- [Google - DSA](https://techdevguide.withgoogle.com/paths/data-structures-and-algorithms/)
- [Illinois - DSA](http://jeffe.cs.illinois.edu/teaching/algorithms/)
- [CrazyProgrammer - Trees](https://www.thecrazyprogrammer.com/2019/09/types-of-trees-in-data-structure.html)
- [Trees - FreeCodeCamp](https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/)
- [binary tree - WikiPedia](https://en.wikipedia.org/wiki/Binary_tree)
- [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree)
- [A* Example by The Coding Train, Jan 16,2017](https://www.youtube.com/watch?v=aKYlikFAV4k)
- [Linked Lists in Python by FreeCodeCamp](https://www.freecodecamp.org/news/introduction-to-linked-lists-in-python/)
- [Structure and Ineterpretation of Computer Programs](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html)
- [Grokking Algorithms by Aditya Bhargava](https://www.goodreads.com/book/show/22847284-grokking-algorithms-an-illustrated-guide-for-programmers-and-other-curio)
- [Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest](https://www.goodreads.com/book/show/6752187-introduction-to-algorithms)
- [The Algorithm Design Manual by Steven Skiena](https://www.goodreads.com/book/show/425208.The_Algorithm_Design_Manual)
- [Reddit List of Algo books](https://www.reddit.com/r/algorithms/comments/i8qb3k/good_books_learning_about_algorithms_from_very/)
- [TheAlgorithms on Github.com](https://github.com/TheAlgorithms)