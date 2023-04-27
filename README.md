# Training

---

## Checkout TDD Challenge

---

## Greetings TDD Challenge

---

## Stacks TDD Challenge

---

## Binary Search TDD Challenge
**Challenge:** Implement a Binary Search Tree Class with Test-Driven Development (TDD)

**Description:**
You are tasked with implementing a Binary Search Tree (BST) data structure in Python. 
A BST is a tree data structure where each node has at most two children, and the left subtree of a node contains only nodes with keys less than the node's key, 
and the right subtree of a node contains only nodes with keys greater than the node's key.

---

### Requirements

#### Development:

- `insert(key):` 
    >Inserts a new node with the given key into the BST.

- `search(key):` 
    >Searches for a node with the given key in the BST and returns its value. Raises an exception if the node is not found.

- `delete(key):` 
    >Deletes the node with the given key from the BST. Raises an exception if the node is not found.

- `is_empty():`  
    >Returns True if the BST is empty, False otherwise.

---

#### Tests: 

- `test_insert():` 
    >Verify that the insert(key) method is working correctly by adding nodes with different keys to the BST and verifying that they are inserted in the correct position according to the BST rules.```

- `test_search():` 
    >Verify that the search(key) method is working correctly by inserting nodes with different keys to the BST and searching for them.

- `test_search_missing_key_raises_exception():` 
    >Verify that calling search(key) on a key that is not in the BST raises an exception.

- `test_delete_leaf_node():` 
    >Verify that the delete(key) method is working correctly by deleting a leaf node from the BST and verifying that it has been removed.

- `test_delete_node_with_one_child():` 
    >Verify that the delete(key) method is working correctly by deleting a node with one child from the BST and verifying that it has been removed and its child has been moved to the correct position.

- `test_delete_node_with_two_children():` 
    >Verify that the delete(key) method is working correctly by deleting a node with two children from the BST and verifying that it has been removed and its successor has been moved to the correct position.

- `test_delete_missing_node_raises_exception():` 
    >Verify that calling delete(key) on a key that is not in the BST raises an exception.

- `test_is_empty():` 
    >Verify that the is_empty() method is working correctly by creating an empty BST and verifying that it returns True, and then inserting a node and verifying that it returns False.