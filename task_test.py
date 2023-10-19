import unittest

# Araba sınıfı, araba özelliklerini ve bilgilerini temsil eder.
class Araba:
    def __init__(self, marka, model, yil, gunluk_ucret):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.gunluk_ucret = gunluk_ucret

# kirala_araba işlevi, bir araba nesnesini ve kiralama tarihlerini alır ve doğrulama yapar.
def kirala_araba(araba, baslangic_tarihi, bitis_tarihi):
    # Araba nesnesinin uygun bir Araba sınıfı örneği olup olmadığını kontrol eder.
    if not isinstance(araba, Araba):
        raise ValueError("Geçersiz araba nesnesi")
    # Tarih formatının uygunluğunu kontrol eder.
    if not isinstance(baslangic_tarihi, str) or not isinstance(bitis_tarihi, str):
        raise ValueError("Geçersiz tarih formatı")

# TestArabaKiralama sınıfı, Araba sınıfı ve kirala_araba işlemini test eder.
class TestArabaKiralama(unittest.TestCase):
    # test_gecersiz_araba_nesnesi işlevi, geçersiz araba nesnesiyle işlemin hatasını test eder.
    def test_gecersiz_araba_nesnesi(self):
        with self.assertRaises(ValueError) as context:
            kirala_araba("Geçersiz Araba", "2023-10-16", "2023-10-18")
        self.assertEqual(str(context.exception), "Geçersiz araba nesnesi")

    # test_gecersiz_tarih_formati işlevi, geçersiz tarih formatıyla işlemin hatasını test eder.
    def test_gecersiz_tarih_formati(self):
        with self.assertRaises(ValueError) as context:
            kirala_araba(Araba("BMW", "X5", 2023, 100), 2023, 2024)
        self.assertEqual(str(context.exception), "Geçersiz tarih formatı")

if __name__ == '__main__':
    unittest.main()
