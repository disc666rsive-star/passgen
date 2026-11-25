import unittest
import string
from main import generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        password = generate_password(16, True, True)
        self.assertEqual(len(password), 16)

    def test_letters_only(self):
        password = generate_password(20, False, False)
        self.assertTrue(password.isalpha())

    def test_without_symbols(self):
        password = generate_password(20, True, False)
        self.assertTrue(password.isalnum())

    def test_allowed_characters(self):
        password = generate_password(20, True, True)
        allowed = string.ascii_letters + string.digits + string.punctuation
        self.assertTrue(all(c in allowed for c in password))


if __name__ == "__main__":
    unittest.main()