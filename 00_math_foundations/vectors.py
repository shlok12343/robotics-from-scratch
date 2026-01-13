import math

"""
Basic vector operations for robotics.
"""

def add(v1, v2):
    """Adds two vectors of the same dimension."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    return [x + y for x, y in zip(v1, v2)]

def subtract(v1, v2):
    """Subtracts v2 from v1."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    return [x - y for x, y in zip(v1, v2)]

def scale(v, s):
    """Scales a vector v by scalar s."""
    return [x * s for x in v]

def dot_product(v1, v2):
    """Calculates the dot product of two vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")
    return sum(x * y for x, y in zip(v1, v2))

def magnitude(v):
    """Calculates the Euclidean norm (length) of a vector."""
    return math.sqrt(sum(x**2 for x in v))

if __name__ == "__main__":
    # Quick test
    a = [3, 4]
    b = [1, 2]
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Dot product (a · b): {dot_product(a, b)}")
    print(f"Magnitude of a: {magnitude(a)}") # Should be 5.0

