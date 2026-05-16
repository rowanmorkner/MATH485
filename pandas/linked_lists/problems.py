"""
Linked List Practice Problems
==============================
Implement each function below. The Node and LinkedList classes are provided
for you -- don't modify them.

Run tests with:  pytest test_problems.py -v
"""


class Node:
    """A single node in a singly linked list."""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """Singly linked list with a head pointer."""
    def __init__(self):
        self.head = None

    def from_list(self, values):
        """Helper: build a linked list from a Python list. [1,2,3] -> 1->2->3->None"""
        for val in reversed(values):
            new_node = Node(val, self.head)
            self.head = new_node
        return self

    def to_list(self):
        """Helper: convert back to a Python list for easy comparison."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def __str__(self):
        return " -> ".join(str(v) for v in self.to_list()) + " -> None"


# =============================================================================
# Problem 1: Length
# Difficulty: Easy
#
# Count the number of nodes in the linked list.
# An empty list has length 0.
# =============================================================================
def length(ll):
    """Return the number of nodes in the linked list.

    Args:
        ll: a LinkedList instance

    Returns:
        int: the number of nodes
    """
    pass


# =============================================================================
# Problem 2: Search
# Difficulty: Easy
#
# Check whether a target value exists anywhere in the list.
# =============================================================================
def search(ll, target):
    """Return True if target exists in the linked list, False otherwise.

    Args:
        ll: a LinkedList instance
        target: the value to search for

    Returns:
        bool
    """
    pass


# =============================================================================
# Problem 3: Append
# Difficulty: Easy
#
# Add a new node with the given value at the END of the list.
# Modify the list in place (don't return anything).
# =============================================================================
def append(ll, val):
    """Append a new node with value val to the end of the linked list.

    Args:
        ll: a LinkedList instance
        val: the value for the new node
    """
    pass


# =============================================================================
# Problem 4: Delete
# Difficulty: Medium
#
# Remove the FIRST node whose value matches the target.
# If the target isn't found, do nothing.
# Handle edge cases: empty list, target at head, target at tail.
# =============================================================================
def delete(ll, target):
    """Delete the first node with value == target from the linked list.

    Args:
        ll: a LinkedList instance
        target: the value to delete
    """
    pass


# =============================================================================
# Problem 5: Get value at index
# Difficulty: Medium
#
# Return the value at position `index` (0-based).
# If the index is out of bounds, raise an IndexError.
# =============================================================================
def get_at_index(ll, index):
    """Return the value at the given index (0-based).

    Args:
        ll: a LinkedList instance
        index: int, the position to retrieve

    Returns:
        the value at that position

    Raises:
        IndexError: if index is out of bounds (including negative indices)
    """
    pass


# =============================================================================
# Problem 6: Reverse
# Difficulty: Medium
#
# Reverse the linked list IN PLACE. Don't create new nodes -- just rewire
# the .next pointers so the list runs backward.
#
# Hint: you need three variables: prev, current, and next_node.
# =============================================================================
def reverse(ll):
    """Reverse the linked list in place.

    Args:
        ll: a LinkedList instance
    """
    pass


# =============================================================================
# Problem 7: Detect cycle
# Difficulty: Hard
#
# Return True if the linked list contains a cycle (a node whose .next
# eventually points back to an earlier node), False otherwise.
#
# Hint: Google "Floyd's tortoise and hare algorithm" if you're stuck.
# The idea -- use two pointers moving at different speeds. If there's a
# cycle, the fast one will eventually lap the slow one.
# =============================================================================
def has_cycle(ll):
    """Return True if the linked list contains a cycle.

    Args:
        ll: a LinkedList instance

    Returns:
        bool
    """
    pass
