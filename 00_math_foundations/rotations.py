import math

"""
Rotation operations for robotics.
Rotations allow us to describe the orientation of a robot or its parts.
"""

def rotate_2d(vector, theta):
    """
    Rotates a 2D vector by angle theta (in radians) counter-clockwise.
    
    The rotation matrix for 2D is:
    [ cos(theta)  -sin(theta) ]
    [ sin(theta)   cos(theta) ]
    """
    if len(vector) != 2:
        raise ValueError("Only 2D vectors are supported for this simple rotation.")
    
    x, y = vector
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    
    new_x = x * cos_t - y * sin_t
    new_y = x * sin_t + y * cos_t
    
    return [new_x, new_y]

if __name__ == "__main__":
    # Test: Rotate [1, 0] by 90 degrees (pi/2 radians)
    point = [1, 0]
    angle = math.pi / 2
    rotated = rotate_2d(point, angle)
    
    print(f"Original: {point}")
    print(f"Rotated by 90 deg: [{rotated[0]:.2f}, {rotated[1]:.2f}]") # Should be [0, 1]

