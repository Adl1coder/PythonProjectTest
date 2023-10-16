import unittest
from email_validator import validate_email, EmailNotValidError

def is_valid_email(address):
    try:
        validate_email(address)
        return True
    except EmailNotValidError:
        return False

class ValidatorsTestCase(unittest.TestCase):
    def test_validate_email(self):
        # Geçerli e-posta adresleri
        self.assertTrue(is_valid_email('birisi@gmail.com'))
        self.assertTrue(is_valid_email('b---i_risi@gmail.com'))

        # Geçersiz e-posta adresleri
        self.assertFalse(is_valid_email('birisi?ulan!@gmail.com'))
        self.assertFalse(is_valid_email('birisigmail.com'))
        self.assertFalse(is_valid_email('@birisigmail.com'))

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().
                                  loadTestsFromTestCase(ValidatorsTestCase))
