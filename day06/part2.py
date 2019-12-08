"""
"""
from typing import Deque, Dict, Optional, Set
from collections import deque


class Node:
    def __init__(
            self,
            value: str = None,
            children: Optional[Set] = None
            ):
        self.value = value
        if children is None:
            self.children: Set[str] = set()


def build_tree_from_input(input_str: str) -> Dict[str, Node]:
    name_to_node: Dict[str, Node] = dict()
    lines = input_str.strip().split('\n')
    for line in lines:
        name, child = line.strip().split(')')
        if name not in name_to_node:
            name_to_node[name] = Node(name)
        name_to_node[name].children.add(child)
        if child not in name_to_node:
            name_to_node[child] = Node(child)
        name_to_node[child].children.add(name)
    return name_to_node


def count_orbital_transfers(
        input_str: str,
        start_node: str = "YOU",
        end_node: str = "SAN"
        ) -> int:
    name_to_node = build_tree_from_input(input_str)
    q: Deque = deque()
    q.append((start_node, -1))
    visited: Set[str] = set()
    while q:
        name, depth = q.popleft()
        if name not in name_to_node or name in visited:
            continue
        visited.add(name)
        for child in name_to_node[name].children:
            if child == end_node:
                return depth
            q.append((child, depth + 1))
    return -1


def test_count_orbital_transfers():
    test_example = """
        COM)B
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        D)I
        E)J
        J)K
        K)L
        K)YOU
        I)SAN
    """.strip()
    assert count_orbital_transfers(test_example) == 4


if __name__ == "__main__":
    test_count_orbital_transfers()
    with open("input") as fin:
        input_str = fin.read()
    print(count_orbital_transfers(input_str))
