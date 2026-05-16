"""
Tests for linked list practice problems.
Run with:  pytest test_problems.py -v
"""
import pytest
from problems import (
    Node,
    LinkedList,
    length,
    search,
    append,
    delete,
    get_at_index,
    reverse,
    has_cycle,
)


# -- Helpers ------------------------------------------------------------------

def make_ll(*values):
    """Shortcut to build a LinkedList from values."""
    ll = LinkedList()
    ll.from_list(list(values))
    return ll


# =============================================================================
# Problem 1: length
# =============================================================================
class TestLength:
    def test_empty(self):
        assert length(LinkedList()) == 0

    def test_single(self):
        assert length(make_ll(42)) == 1

    def test_multiple(self):
        assert length(make_ll(1, 2, 3, 4, 5)) == 5

    def test_doesnt_mutate(self):
        ll = make_ll(1, 2, 3)
        length(ll)
        assert ll.to_list() == [1, 2, 3]


# =============================================================================
# Problem 2: search
# =============================================================================
class TestSearch:
    def test_empty(self):
        assert search(LinkedList(), 5) is False

    def test_found_at_head(self):
        assert search(make_ll(10, 20, 30), 10) is True

    def test_found_at_tail(self):
        assert search(make_ll(10, 20, 30), 30) is True

    def test_found_in_middle(self):
        assert search(make_ll(10, 20, 30), 20) is True

    def test_not_found(self):
        assert search(make_ll(10, 20, 30), 99) is False

    def test_searches_strings(self):
        assert search(make_ll("a", "b", "c"), "b") is True


# =============================================================================
# Problem 3: append
# =============================================================================
class TestAppend:
    def test_append_to_empty(self):
        ll = LinkedList()
        append(ll, 1)
        assert ll.to_list() == [1]

    def test_append_to_nonempty(self):
        ll = make_ll(1, 2)
        append(ll, 3)
        assert ll.to_list() == [1, 2, 3]

    def test_append_multiple(self):
        ll = LinkedList()
        append(ll, "x")
        append(ll, "y")
        append(ll, "z")
        assert ll.to_list() == ["x", "y", "z"]


# =============================================================================
# Problem 4: delete
# =============================================================================
class TestDelete:
    def test_delete_from_empty(self):
        ll = LinkedList()
        delete(ll, 5)  # should not raise
        assert ll.to_list() == []

    def test_delete_head(self):
        ll = make_ll(1, 2, 3)
        delete(ll, 1)
        assert ll.to_list() == [2, 3]

    def test_delete_tail(self):
        ll = make_ll(1, 2, 3)
        delete(ll, 3)
        assert ll.to_list() == [1, 2]

    def test_delete_middle(self):
        ll = make_ll(1, 2, 3)
        delete(ll, 2)
        assert ll.to_list() == [1, 3]

    def test_delete_not_found(self):
        ll = make_ll(1, 2, 3)
        delete(ll, 99)
        assert ll.to_list() == [1, 2, 3]

    def test_delete_only_first_occurrence(self):
        ll = make_ll(1, 2, 2, 3)
        delete(ll, 2)
        assert ll.to_list() == [1, 2, 3]

    def test_delete_single_element(self):
        ll = make_ll(42)
        delete(ll, 42)
        assert ll.to_list() == []


# =============================================================================
# Problem 5: get_at_index
# =============================================================================
class TestGetAtIndex:
    def test_first_element(self):
        assert get_at_index(make_ll(10, 20, 30), 0) == 10

    def test_last_element(self):
        assert get_at_index(make_ll(10, 20, 30), 2) == 30

    def test_middle_element(self):
        assert get_at_index(make_ll(10, 20, 30), 1) == 20

    def test_out_of_bounds(self):
        with pytest.raises(IndexError):
            get_at_index(make_ll(10, 20), 5)

    def test_negative_index(self):
        with pytest.raises(IndexError):
            get_at_index(make_ll(10, 20), -1)

    def test_empty_list(self):
        with pytest.raises(IndexError):
            get_at_index(LinkedList(), 0)


# =============================================================================
# Problem 6: reverse
# =============================================================================
class TestReverse:
    def test_empty(self):
        ll = LinkedList()
        reverse(ll)
        assert ll.to_list() == []

    def test_single(self):
        ll = make_ll(1)
        reverse(ll)
        assert ll.to_list() == [1]

    def test_two_elements(self):
        ll = make_ll(1, 2)
        reverse(ll)
        assert ll.to_list() == [2, 1]

    def test_multiple(self):
        ll = make_ll(1, 2, 3, 4, 5)
        reverse(ll)
        assert ll.to_list() == [5, 4, 3, 2, 1]

    def test_double_reverse_restores(self):
        ll = make_ll(1, 2, 3)
        reverse(ll)
        reverse(ll)
        assert ll.to_list() == [1, 2, 3]


# =============================================================================
# Problem 7: has_cycle
# =============================================================================
class TestHasCycle:
    def test_empty(self):
        assert has_cycle(LinkedList()) is False

    def test_single_no_cycle(self):
        assert has_cycle(make_ll(1)) is False

    def test_no_cycle(self):
        assert has_cycle(make_ll(1, 2, 3, 4)) is False

    def test_cycle_to_head(self):
        """Tail points back to head: 1 -> 2 -> 3 -> (back to 1)"""
        ll = make_ll(1, 2, 3)
        # Manually create the cycle
        tail = ll.head.next.next  # node with val 3
        tail.next = ll.head       # point tail back to head
        assert has_cycle(ll) is True

    def test_cycle_to_middle(self):
        """Tail points to middle: 1 -> 2 -> 3 -> (back to 2)"""
        ll = make_ll(1, 2, 3)
        middle = ll.head.next     # node with val 2
        tail = middle.next        # node with val 3
        tail.next = middle        # point tail back to middle
        assert has_cycle(ll) is True

    def test_self_cycle(self):
        """Single node points to itself."""
        ll = LinkedList()
        ll.head = Node(1)
        ll.head.next = ll.head
        assert has_cycle(ll) is True
