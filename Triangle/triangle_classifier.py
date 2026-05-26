"""Triangle classification module."""


def classify_triangle(a, b, c):
    """Classify a triangle from three side lengths.

    Returns one of:
    - "Invalid Input"
    - "Not a Triangle"
    - "Equilateral"
    - "Isosceles"
    - "Scalene"
    """

    sides = (a, b, c)
    if any(not isinstance(side, int) or side < 1 or side > 100 for side in sides):
        return "Invalid Input"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a Triangle"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Isosceles"

    return "Scalene"