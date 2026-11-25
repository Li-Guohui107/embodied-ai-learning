"""Planar 2-DOF arm kinematics. Standard-library only."""

from math import acos, atan2, cos, sin


def forward_kinematics(theta1, theta2, link1=1.0, link2=1.0):
    """Return (x, y) for a planar two-link arm. Angles are radians."""
    if link1 <= 0 or link2 <= 0:
        raise ValueError("Link lengths must be positive.")
    x = link1 * cos(theta1) + link2 * cos(theta1 + theta2)
    y = link1 * sin(theta1) + link2 * sin(theta1 + theta2)
    return x, y


def inverse_kinematics(x, y, link1=1.0, link2=1.0, elbow_up=False):
    """Return one IK solution. Raises ValueError for unreachable targets.

    elbow_up=False selects positive theta2; elbow_up=True selects negative theta2.
    This simple example does not enforce joint limits or collision constraints.
    """
    if link1 <= 0 or link2 <= 0:
        raise ValueError("Link lengths must be positive.")

    cos_theta2 = (
        x * x + y * y - link1 * link1 - link2 * link2
    ) / (2.0 * link1 * link2)

    tol = 1e-12
    if cos_theta2 < -1.0 - tol or cos_theta2 > 1.0 + tol:
        raise ValueError("Target is outside the reachable workspace.")

    cos_theta2 = max(-1.0, min(1.0, cos_theta2))
    theta2_abs = acos(cos_theta2)
    theta2 = -theta2_abs if elbow_up else theta2_abs

    k1 = link1 + link2 * cos(theta2)
    k2 = link2 * sin(theta2)
    theta1 = atan2(y, x) - atan2(k2, k1)
    return theta1, theta2


def main():
    from math import pi

    link1, link2 = 1.0, 0.8
    theta1, theta2 = pi / 6, pi / 3
    x, y = forward_kinematics(theta1, theta2, link1, link2)

    print("Planar 2-DOF arm")
    print(f"Joint angles: theta1={theta1:.4f} rad, theta2={theta2:.4f} rad")
    print(f"End-effector: x={x:.4f}, y={y:.4f}")

    recovered = inverse_kinematics(x, y, link1, link2)
    check = forward_kinematics(*recovered, link1, link2)
    print(f"IK solution: theta1={recovered[0]:.4f}, theta2={recovered[1]:.4f}")
    print(f"FK verification: x={check[0]:.4f}, y={check[1]:.4f}")


if __name__ == "__main__":
    main()
