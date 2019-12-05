"""
--- Day 3: Crossed Wires ---

The gravity assist was successful, and you're well on your way to the Venus
refuelling station. During the rush back on Earth, the fuel management system
wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are
connected to a central port and extend outward on a grid. You trace the path
each wire takes as it leaves the central port, one wire per line of text (your
puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix
the circuit, you need to find the intersection point closest to the central
port. Because the wires are on a grid, use the Manhattan distance for this
measurement. While the wires do technically cross right at the central port
where they both start, this point does not count, nor does a wire count as
crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the
central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........

Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4,
and left 4:

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

These wires cross at two locations (marked X), but the lower-left one is
closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

- R75,D30,R83,U83,L12,D49,R71,U7,L72
  U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

- R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
  U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

What is the Manhattan distance from the central port to the closest
intersection?
"""


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

    def _manhattan_distance(x, y):
        return abs(x) + abs(y)

    visited = set()
    x, y = 0, 0
    for move in wire1.split(','):
        direction, distance = _parse_move(move)
        for _ in range(distance):
            x, y = _single_move(direction, x, y)
            visited.add((x, y))

    min_dist = float("inf")
    x, y = 0, 0
    for move in wire2.split(','):
        direction, distance = _parse_move(move)
        for _ in range(distance):
            x, y = _single_move(direction, x, y)
            if (x, y) in visited:
                min_dist = min(min_dist, _manhattan_distance(x, y))

    return min_dist


def test_find_distance_to_closest_intersection():
    wire1 = "R8,U5,L5,D3"
    wire2 = "U7,R6,D4,L4"
    assert find_distance_to_closest_intersection(wire1, wire2) == 6

    wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    assert find_distance_to_closest_intersection(wire1, wire2) == 159

    wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    assert find_distance_to_closest_intersection(wire1, wire2) == 135

    print("All tests passed.")


if __name__ == "__main__":
    test_find_distance_to_closest_intersection()

    with open("input") as fin:
        lines = fin.read()

    wire1, wire2 = lines.strip().split('\n')
    print(find_distance_to_closest_intersection(wire1, wire2))
