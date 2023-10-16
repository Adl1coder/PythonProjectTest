import unittest

class Araba:
    def __init__(self, marka, model, yil, gunluk_ucret):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.gunluk_ucret = gunluk_ucret

def kirala_araba(araba, baslangic_tarihi, bitis_tarihi):
    if not isinstance(araba, Araba):
        raise ValueError("Geçersiz araba nesnesi")
    if not isinstance(baslangic_tarihi, str) or not isinstance(bitis_tarihi, str):
        raise ValueError("Geçersiz tarih formatı")


class TestArabaKiralama(unittest.TestCase):
    def test_gecersiz_araba_nesnesi(self):
        with self.assertRaises(ValueError) as context:
            kirala_araba("Geçersiz Araba", "2023-10-16", "2023-10-18")
        self.assertEqual(str(context.exception), "Geçersiz araba nesnesi")

    def test_gecersiz_tarih_formati(self):
        with self.assertRaises(ValueError) as context:
            kirala_araba(Araba("BMW", "X5", 2023, 100), 2023, 2024)
        self.assertEqual(str(context.exception), "Geçersiz tarih formatı")

if __name__ == '__main__':
    unittest.main()
