"""
--- Day 6: Universal Orbit Map ---

You've landed at the Universal Orbit Map facility on Mercury. Because
navigation in space often involves transferring between orbits, the orbit maps
here are useful for finding efficient routes between, for example, you and
Santa. You download a map of the local orbits (your puzzle input).

Except for the universal Center of Mass (COM), every object in space is in
orbit around exactly one other object. An orbit looks roughly like this:

                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /

In this diagram, the object BBB is in orbit around AAA. The path that BBB
takes around AAA (drawn with lines) is only partly shown. In the map data,
this orbital relationship is written AAA)BBB, which means "BBB is in orbit
around AAA".

Before you use your map data to plot a course, you need to make sure it wasn't
corrupted during the download. To verify maps, the Universal Orbit Map
facility uses orbit count checksums - the total number of direct orbits (like
the one shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can
be any number of objects long: if A orbits B, B orbits C, and C orbits D, then
A indirectly orbits D.

For example, suppose you have the following map:

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

Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I

In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

- D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
- L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of
  7 orbits.
- COM orbits nothing.

The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?
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
    return name_to_node


def count_orbits(input_str) -> int:
    name_to_node = build_tree_from_input(input_str)
    count = 0
    q: Deque = deque()
    q.append(("COM", 0))
    while q:
        name, depth = q.popleft()
        count += depth
        if name not in name_to_node:
            continue
        for child in name_to_node[name].children:
            q.append((child, depth + 1))
    return count


def test_count_orbits():
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
    """.strip()
    assert count_orbits(test_example) == 42


if __name__ == "__main__":
    test_count_orbits()
    with open("input") as fin:
        input_str = fin.read()
    print(count_orbits(input_str))
