from linked_list import LinkedList
from typing import Any


def partition(ll: LinkedList, x: Any) -> LinkedList:
    # Create new linked list that will store partitioned values
    partitioned_ll = LinkedList([x]) 입력 : 3 → 5 → 8 → 5 → 10 → 2 → 1 [분할값 x = 5]

    # Start with head
    current_node = ll.head

    # Finish until current node is None <=> reached tail of ll
    while current_node:
        # If value of current node is smaller than x,
        if current_node.value < x:
            # add current value at the head of linked list
            partitioned_ll.add_to_beginning(current_node.value)
        # If value of current node is larger or equal to x,
        else:
            # add current value at the end of linked list
            partitioned_ll.add(current_node.value)
        # update current node as next node of
        current_node = current_node.next

    return partitioned_ll


def example():
    # Generate linked list of size 10, with random number at 0-99
    ll = LinkedList.generate(10, 0, 99)
    x = 50

    print(f"Patitioning following list by value {x}")
    print(ll)
    partitioned_ll = partition(ll, x)

    print("\nAfter partitioning")
    print(partitioned_ll)


if __name__ == "__main__":
    example()