import unittest

# Test edilecek fonksiyon
def topla(x, y):
    return x + y

# Test sınıfı
class TestToplama(unittest.TestCase):
    def test_topla_pozitif(self):
        self.assertEqual(topla(5, 3), 8)

    def test_topla_negatif(self):
        self.assertEqual(topla(-5, -3), -8)

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestToplama))
