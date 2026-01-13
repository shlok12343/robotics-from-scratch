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

def normalize(v):
    """Returns the unit vector in the same direction as v."""
    m = magnitude(v)
    if m == 0:
        raise ValueError("Cannot normalize a zero vector")
    return scale(v, 1.0 / m)

def cross_product(v1, v2):
    """
    Calculates the cross product of two 3D vectors.
    Returns a vector perpendicular to both v1 and v2.
    """
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product is only defined for 3D vectors in this implementation.")
    
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

if __name__ == "__main__":
    # Quick test
    a = [3, 4, 0]
    b = [1, 2, 0]
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Dot product (a · b): {dot_product(a, b)}")
    print(f"Magnitude of a: {magnitude(a)}")
    print(f"Unit vector of a: {normalize(a)}")
    
    # 3D Cross product test (X cross Y = Z)
    x_axis = [1, 0, 0]
    y_axis = [0, 1, 0]
    print(f"Cross product (X × Y): {cross_product(x_axis, y_axis)}")

