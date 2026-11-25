import math
import unittest

from kinematics import forward_kinematics, inverse_kinematics


class TestPlanarArm(unittest.TestCase):
    def test_fk_ik_fk_round_trip(self):
        l1, l2 = 1.0, 0.8
        x, y = forward_kinematics(math.radians(25), math.radians(70), l1, l2)
        q1, q2 = inverse_kinematics(x, y, l1, l2)
        x2, y2 = forward_kinematics(q1, q2, l1, l2)
        self.assertAlmostEqual(x, x2, places=9)
        self.assertAlmostEqual(y, y2, places=9)

    def test_elbow_branches_reach_same_target(self):
        l1, l2 = 1.0, 0.8
        target = (1.0, 0.5)
        q_down = inverse_kinematics(*target, l1, l2, elbow_up=False)
        q_up = inverse_kinematics(*target, l1, l2, elbow_up=True)
        for actual in (
            forward_kinematics(*q_down, l1, l2),
            forward_kinematics(*q_up, l1, l2),
        ):
            self.assertAlmostEqual(actual[0], target[0], places=9)
            self.assertAlmostEqual(actual[1], target[1], places=9)

    def test_unreachable_target_raises(self):
        with self.assertRaises(ValueError):
            inverse_kinematics(10.0, 10.0, 1.0, 1.0)

    def test_invalid_link_length_raises(self):
        with self.assertRaises(ValueError):
            forward_kinematics(0.0, 0.0, 0.0, 1.0)


if __name__ == "__main__":
    unittest.main()
