import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        password = generate_password(12, 4, 4, 2, 2)
        self.assertEqual(len(password), 12)

    def test_generate_password_character_types(self):
        password = generate_password(16, 4, 4, 4, 4)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(not c.isalnum() for c in password))

if __name__ == '__main__':
    unittest.main()
