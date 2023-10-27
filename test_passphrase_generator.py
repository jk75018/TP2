import unittest
from passphrase_generator import generate_random_passphrase

class TestPassphraseGenerator(unittest.TestCase):

    def test_passphrase_word_count(self):
        passphrase = generate_random_passphrase(5)
        words = passphrase.split()
        self.assertEqual(len(words), 5)

    def test_passphrase_word_length(self):
        passphrase = generate_random_passphrase(5)
        words = passphrase.split()
        self.assertTrue(all(len(word) >= 3 for word in words))

if __name__ == '__main__':
    unittest.main()
