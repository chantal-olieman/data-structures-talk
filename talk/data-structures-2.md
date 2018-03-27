# Data Structures (part 2)

## Trees and Graphs

---

# Content
- Recap
- Nodes
- Trees
- Tree traversal
- Graphs
- Graph representation
- Dijkstra
- (Heaps)

---

# Recap
## Big O notation

O($n$) where $n$ is the order of the input
```python
for i in list:
	#do something
n = len(list)
```
O($n^2$)
```python
for i in list:
	for i in list:
    		#do something
```
O($n^2$) + O($n$) $=$ O($n^2$)


---
# Nodes
- value
- pointer


```
class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node
```

---

---
# Data structures
## Linked lists, stack and queue

A stored link list contains just the head:
```
class LinkedList:
    def __init__(self, head):
        self.head = head # contains the first node in the list
```
---
## Stack and queue
- In Python
- Complexity

![](sq.jpg)

---

## Hashmap and Set
- In Python
- Complexity
- --

|                       | array list (list) | queue | stack | hash map (dict) | set |
|:---------------------:|:-----------------:|:-----:|:-----:|:---------------:|:---------------:|
|      add element      |        O(1)       |  O(1) |  O(1) |       O(1)      |O(1) |
|     remove element    |        O(n)       |  O(1) |  O(1) |       O(1)      | O(1)|
| find element at index |        O(1)       |  O(n) |  O(n) |      -      | - |
| find element          |        O(n)       |  O(n) |  O(n) |       O(1)      |O(1) |

---
# Trees
Binary tree:              

![Binary tree](tree.png) ![Non binary tree](tree2.png)

---
# Trees
## Implementation in python
```
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data # contains the data
        self.left = None # contains the reference to the left child
        self.right = None # contains the reference to the right child
```
```
class TreeNode:
    def __init__(self, data):
        self.data = data # contains the data
        self.cilderen = [] # contains a list with childeren
```
---
# Try yourself!
`input:` the root of a binary tree

`output:` a list containing all nodes by level, starting from the root.

![Binary tree](bt.png)

`result: [2, 7, 5, 2, 6, 9, 5, 11, 4]`

---
# BFS & DFS
- **Breadth first search**
Start with the closest nodes first
- **Depth fitst search**
Start with one node and go as deep as possible into its children
![dfs](bfs-dfs.png)
---
# BFS & DFS
## Implementations

---
# Graphs
![](g-t.png)

---
# Application
### Trees
### Graphs
---
# Application
### Trees
- File system
- Sorting of sorted Data
- Manipulate Hierarchical Data
- Faster Lookup

### Graphs
- Social relations (facebook)
- Maps (google maps, shortest path, Dijkstra)
- Recommendations ("you might also like..")
