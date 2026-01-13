import matplotlib.pyplot as plt
from vectors import add, rotate_2d
import math

"""
A simple script to visualize vector operations.
Requires: pip install matplotlib
"""

def plot_vectors():
    # Define some base vectors
    v1 = [2, 1]
    v2 = [1, 2]
    
    # Operation 1: Addition
    v_sum = add(v1, v2)
    
    # Operation 2: Rotation
    angle = math.pi / 4  # 45 degrees
    v_rot = rotate_2d(v1, angle)
    
    # Setup the plot
    plt.figure(figsize=(6, 6))
    ax = plt.gca()
    
    # Plotting helper
    def draw_vec(v, origin=[0, 0], color='blue', label=None):
        plt.quiver(*origin, v[0], v[1], color=color, angles='xy', scale_units='xy', scale=1, label=label)

    draw_vec(v1, color='blue', label='v1')
    draw_vec(v2, color='green', label='v2')
    draw_vec(v_sum, color='red', label='v1 + v2')
    draw_vec(v_rot, color='orange', label='v1 rotated 45°')

    # Formatting
    plt.xlim(-1, 5)
    plt.ylim(-1, 5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.legend()
    plt.title("Robotics Math: Vector Visualization")
    
    print("Plotting vectors... (Close the window to continue)")
    plt.show()

if __name__ == "__main__":
    plot_vectors()

