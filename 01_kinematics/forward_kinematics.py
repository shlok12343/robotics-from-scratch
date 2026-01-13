import math

"""
Forward Kinematics for a 2-link robotic arm.
Forward kinematics is the process of calculating the position of the end-effector
(the robot's 'hand') given the joint angles.
"""

class TwoLinkArm:
    def __init__(self, link1_length, link2_length):
        """
        Initializes the arm with two links of given lengths.
        
        :param link1_length: Length of the first link (connected to base)
        :param link2_length: Length of the second link (connected to end-effector)
        """
        self.l1 = link1_length
        self.l2 = link2_length
        
        # Current joint angles in radians
        self.theta1 = 0.0
        self.theta2 = 0.0

    def set_angles(self, theta1, theta2):
        """Sets the joint angles of the arm."""
        self.theta1 = theta1
        self.theta2 = theta2

    def calculate_forward_kinematics(self):
        """
        Calculates the (x, y) position of the end-effector.
        Logic to be implemented in the next step.
        """
        pass

if __name__ == "__main__":
    # Initialize an arm with link lengths of 1.0 and 1.0
    arm = TwoLinkArm(1.0, 1.0)
    print(f"Initialized 2-link arm with lengths: L1={arm.l1}, L2={arm.l2}")
    print(f"Initial joint angles: theta1={arm.theta1}, theta2={arm.theta2}")

