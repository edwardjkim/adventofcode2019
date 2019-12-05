"""
--- Part Two ---

An Elf just remembered one more important detail: the two adjacent matching
digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the
following are now true:

- 112233 meets these criteria because the digits never decrease and all
  repeated digits are exactly two digits long.
- 123444 no longer meets the criteria (the repeated 44 is part of a larger
  group of 444).
- 111122 meets the criteria (even though 1 is repeated more than twice, it
  still contains a double 22).

How many different passwords within the range given in your puzzle input meet
all of the criteria?
"""
from collections import Counter
import part1


def meets_criteria(n: int) -> bool:
    if not part1.meets_criteria(n):
        return False

    char_counter = Counter(str(n))
    values_counter = Counter(char_counter.values())
    return values_counter[2] >= 1


assert meets_criteria(112233) is True
assert meets_criteria(123444) is False
assert meets_criteria(111122) is True


def find_brute_force(start: int, end: int) -> int:
    count = 0
    for i in range(max(start, 10**5), min(end + 1, 10**6)):
        if meets_criteria(i):
            count += 1
    return count


if __name__ == "__main__":
    print(find_brute_force(372304, 847060))
