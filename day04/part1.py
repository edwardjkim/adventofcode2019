"""
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a
password. The Elves had written the password on a sticky note, but someone
threw it out.

However, they do remember a few key facts about the password:

- It is a six-digit number.
- The value is within the range given in your puzzle input.
- Two adjacent digits are the same (like 22 in 122345).
- Going from left to right, the digits never decrease; they only ever increase
  or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

- 111111 meets these criteria (double 11, never decreases).
- 223450 does not meet these criteria (decreasing pair of digits 50).
- 123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet
these criteria?
"""


def meets_criteria(n: int) -> bool:
    s = str(n)
    same_chars_adjacent = False
    for first_char, second_char in zip(s[:-1], s[1:]):
        if first_char > second_char:
            return False
        if first_char == second_char:
            same_chars_adjacent = True
    return same_chars_adjacent


assert meets_criteria(111111) is True
assert meets_criteria(223450) is False
assert meets_criteria(123789) is False


def find_brute_force(start: int, end: int) -> int:
    count = 0
    for i in range(max(start, 10**5), min(end + 1, 10**6)):
        if meets_criteria(i):
            count += 1
    return count


if __name__ == "__main__":
    print(find_brute_force(372304, 847060))
