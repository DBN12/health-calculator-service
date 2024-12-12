import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        # Test basique
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.857142857, places=2)
        # Test avec des valeurs plus petites
        self.assertAlmostEqual(calculate_bmi(1.60, 50), 19.53, places=2)
        
        # Test des erreurs
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)
        with self.assertRaises(ValueError):
            calculate_bmi(1.75, -10)

    def test_calculate_bmr_male(self):
        self.assertAlmostEqual(calculate_bmr(180, 75, 25, "male"), 1815.03, places=2)
        
    def test_calculate_bmr_female(self):
        self.assertAlmostEqual(calculate_bmr(165, 60, 30, "female"), 1383.68, places=2)
        
        # Test des erreurs
        with self.assertRaises(ValueError):
            calculate_bmr(-165, 60, 30, "female")
        with self.assertRaises(ValueError):
            calculate_bmr(165, 0, 30, "female")
        with self.assertRaises(ValueError):
            calculate_bmr(165, 60, 30, "other")

if __name__ == '__main__':
    unittest.main()
