# Linked Lists in Python

## Why linked lists?

Python's built-in `list` is secretly an **array** under the hood -- a contiguous block of
memory where elements sit side-by-side. This is great for random access (`lst[i]` is O(1)),
but painful when you need to insert or delete in the middle: every element after the change
has to shift over (O(n)).

A **linked list** trades away random access for efficient insertion/deletion. Each element
(called a **node**) stores its value *and* a reference to the next node. Nodes can live
anywhere in memory -- they're stitched together by pointers, not by position.

```
Array/Python list:
[ 10 | 20 | 30 | 40 ]   <- contiguous memory, indexed by position

Linked list:
[10|->] --> [20|->] --> [30|->] --> [40|None]   <- scattered in memory, connected by references
```

### When would you actually use one?

| Use case | Winner |
|---|---|
| Access element by index | Array |
| Iterate through everything | Tie |
| Insert/delete at the front | Linked list (O(1) vs O(n)) |
| Insert/delete in the middle (given a reference) | Linked list (O(1) vs O(n)) |
| Memory efficiency for small data | Array (no pointer overhead) |
| Building queues, undo stacks, LRU caches | Linked list |

In practice you'll rarely reach for a linked list in day-to-day Python/data science work --
Python lists and `collections.deque` cover most needs. But linked lists are **foundational**
for understanding pointers/references, recursive thinking, and how higher-level data
structures work internally.

---

## Building block: the Node

A linked list is just a chain of nodes. Each node holds two things:

1. **`val`** -- the data
2. **`next`** -- a reference to the next node (or `None` if it's the last one)

```python
class Node:
    """A single node in a singly linked list."""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
```

That's it. You can already build a list by hand:

```python
# Build: 1 -> 2 -> 3
c = Node(3)          # tail node
b = Node(2, c)       # middle, points to c
a = Node(1, b)       # head, points to b
```

The variable `a` is the **head** -- it's your entry point to the entire list. There's no
"list object" yet, just nodes pointing to each other.

---

## Traversal: walking the chain

To visit every node, start at the head and follow `.next` until you hit `None`:

```python
def print_list(head):
    """Walk the list and print each value."""
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Using our nodes from above:
print_list(a)
# Output: 1 -> 2 -> 3 -> None
```

**Key pattern:** `current = current.next` is how you advance through a linked list.
You'll see this in virtually every linked list operation.

---

## The LinkedList class

Wrapping things in a class gives us a clean API and keeps track of the head for us:

```python
class LinkedList:
    """Singly linked list."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, val):
        """Insert at the front -- O(1)."""
        new_node = Node(val, self.head)  # new node points to old head
        self.head = new_node             # new node becomes the head

    def append(self, val):
        """Insert at the end -- O(n) because we have to walk to the tail."""
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            return
        # Walk to the last node
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node  # tack it on at the end

    def __str__(self):
        """Pretty-print the list."""
        parts = []
        current = self.head
        while current:
            parts.append(str(current.val))
            current = current.next
        return " -> ".join(parts) + " -> None"
```

Usage:

```python
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
print(ll)
# Output: 5 -> 10 -> 20 -> None
```

### Why is prepend O(1) but append O(n)?

**Prepend** only touches the head -- you create a node, point it at the old head, done.

**Append** has to walk the entire chain to find the tail. You *could* fix this by also
storing a `self.tail` pointer, but that adds bookkeeping to every operation.

---

## Core operations

### Search -- does a value exist?

```python
def search(self, target):
    """Return True if target is in the list."""
    current = self.head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False
```

**Time:** O(n) -- worst case you check every node.

### Delete -- remove the first occurrence of a value

This is where linked lists get interesting. You need to handle three cases:

```python
def delete(self, target):
    """Remove the first node with value == target."""
    # Case 1: empty list
    if self.is_empty():
        return

    # Case 2: target is at the head
    if self.head.val == target:
        self.head = self.head.next  # skip over the head
        return

    # Case 3: target is somewhere in the middle/end
    current = self.head
    while current.next is not None:
        if current.next.val == target:
            current.next = current.next.next  # skip over the target node
            return
        current = current.next
```

**The trick:** to delete a node, you need a reference to the node *before* it, so you can
rewire `previous.next` to skip over the doomed node.

```
Before delete(20):
[10|->] --> [20|->] --> [30|->] --> None

After delete(20):
[10|->] ---------> [30|->] --> None
         (20 is now unreachable, garbage collected)
```

### Get length

```python
def length(self):
    """Count the nodes."""
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count
```

### Reverse

Reversing a linked list is a classic interview question. The idea: walk through the list,
flipping each node's `.next` pointer to point backward.

```python
def reverse(self):
    """Reverse the list in place."""
    prev = None
    current = self.head
    while current:
        next_node = current.next   # save the next node before we break the link
        current.next = prev        # flip the pointer
        prev = current             # advance prev
        current = next_node        # advance current
    self.head = prev               # prev is now the new head
```

Walk through it with `1 -> 2 -> 3`:

| Step | prev | current | next_node | Action |
|------|------|---------|-----------|--------|
| 0 | None | 1 | 2 | 1.next = None |
| 1 | 1 | 2 | 3 | 2.next = 1 |
| 2 | 2 | 3 | None | 3.next = 2 |
| done | 3 | None | -- | head = 3 |

Result: `3 -> 2 -> 1 -> None`

---

## Recursive thinking

Linked lists are naturally recursive -- a linked list is either:
- **Empty** (`None`), or
- **A node** followed by **another linked list**

This means many operations have elegant recursive solutions:

```python
def search_recursive(node, target):
    """Recursively search for target starting from node."""
    # Base case: reached the end
    if node is None:
        return False
    # Base case: found it
    if node.val == target:
        return True
    # Recursive case: check the rest of the list
    return search_recursive(node.next, target)
```

The recursive pattern is always: handle `None`, handle the current node, recurse on
`node.next`.

---

## Common pitfalls

1. **Losing the head.** If you reassign `self.head` by accident during traversal, you've
   lost the whole list. Always use a `current` variable to walk.

2. **Off-by-one with `None`.** Check `current is not None` vs `current.next is not None` --
   they stop at different places. The first visits every node; the second stops one early
   (useful for delete/insert operations where you need the *previous* node).

3. **Forgetting edge cases.** Always consider: empty list, single-node list, target at head,
   target at tail, target not present.

4. **Infinite loops.** If you forget `current = current.next`, you'll loop forever on the
   same node.

---

## Quick reference

| Operation | Time | Notes |
|-----------|------|-------|
| Prepend | O(1) | Just rewire the head |
| Append | O(n) | Walk to the end (O(1) with tail pointer) |
| Search | O(n) | Linear scan |
| Delete (given value) | O(n) | Find it, then rewire |
| Delete (given node ref) | O(1) | Just rewire pointers |
| Access by index | O(n) | No random access! |
| Reverse | O(n) | Single pass, three pointers |

---

## What's next?

The practice problems in `problems.py` have you implement these operations yourself.
Run `pytest test_problems.py -v` to check your work. They're ordered from easiest to
hardest -- start at the top and work down.

Once you're comfortable with singly linked lists, the natural extensions are:
- **Doubly linked lists** -- each node also has a `.prev` pointer (easier deletes, more memory)
- **Circular linked lists** -- the tail points back to the head
- **Python's `collections.deque`** -- a doubly linked list under the hood
