"""
Basic vector operations for robotics.
Robotics relies heavily on linear algebra. Understanding how to manipulate 
position and velocity vectors is the first step.
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

if __name__ == "__main__":
    # Quick test
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"Add: {add(a, b)}")
    print(f"Subtract: {subtract(a, b)}")
    print(f"Scale (2x): {scale(a, 2)}")

