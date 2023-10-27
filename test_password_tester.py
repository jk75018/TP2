import unittest
from password_tester import test_password_strength

class TestPasswordTester(unittest.TestCase):

    def test_weak_password(self):
        entropy, strength = test_password_strength("weakpass123")
        self.assertEqual(strength, "Faible")

    def test_strong_password(self):
        entropy, strength = test_password_strength("Str0ngP@ssw0rd")
        self.assertEqual(strength, "Fort")

if __name__ == '__main__':
    unittest.main()
