"""
--- Part Two ---

It turns out that this circuit is very timing-sensitive; you actually need to
minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each
intersection; choose the intersection where the sum of both wires' steps is
lowest. If a wire visits a position on the grid multiple times, use the steps
value from the first time it visits that position when calculating the total
value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire
has entered to get to that location, including the intersection being
considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........

In the above example, the intersection closest to the central port is reached
after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second
wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2
= 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

- R75,D30,R83,U83,L12,D49,R71,U7,L72
  U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps

- R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
  U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

What is the fewest combined steps the wires must take to reach an intersection?
"""
from typing import Dict, Tuple


def find_distance_to_closest_intersection(wire1: str, wire2: str) -> float:

    def _single_move(direction, x, y):
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        else:
            raise ValueError
        return x, y

    def _parse_move(move_string):
        direction, distance = move[0], int(move[1:])
        return direction, distance

    visited: Dict[Tuple[int, int], int] = dict()
    x, y, steps = 0, 0, 0
    for move in wire1.split(','):
        direction, distance = _parse_move(move)
        for _ in range(distance):
            x, y = _single_move(direction, x, y)
            steps += 1
            if (x, y) not in visited:
                visited[x, y] = steps

    min_dist = float("inf")
    x, y, steps = 0, 0, 0
    for move in wire2.split(','):
        direction, distance = _parse_move(move)
        for _ in range(distance):
            x, y = _single_move(direction, x, y)
            steps += 1
            if (x, y) in visited:
                min_dist = min(min_dist, visited[x, y] + steps)

    return min_dist


def test_find_distance_to_closest_intersection():
    wire1 = "R8,U5,L5,D3"
    wire2 = "U7,R6,D4,L4"
    assert find_distance_to_closest_intersection(wire1, wire2) == 30

    wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    assert find_distance_to_closest_intersection(wire1, wire2) == 610

    wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    assert find_distance_to_closest_intersection(wire1, wire2) == 410

    print("All tests passed.")


if __name__ == "__main__":
    test_find_distance_to_closest_intersection()

    with open("input") as fin:
        lines = fin.read()

    wire1, wire2 = lines.strip().split('\n')
    print(find_distance_to_closest_intersection(wire1, wire2))
