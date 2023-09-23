import unittest
import sys
import pandas as pd
sys.path.append(r'C:\Users\LUV\T')
from Algorithm_Functions import find_support_resistance_levels 

class TestFindSupportResistanceLevels(unittest.TestCase):

    def test_empty_dataframe(self):
        df = pd.DataFrame()
        support_levels, resistance_levels = find_support_resistance_levels(df)
        self.assertEqual(support_levels, [])
        self.assertEqual(resistance_levels, [])

    def test_no_support_or_resistance(self):
        data = {'Date': [1, 2, 3, 4, 5],
                'High': [50, 55, 53, 56, 52],
                'Low': [45, 48, 47, 49, 46]}
        df = pd.DataFrame(data)
        support_levels, resistance_levels = find_support_resistance_levels(df)
        self.assertEqual(support_levels, [])
        self.assertEqual(resistance_levels, [])

    def test_support_and_resistance_levels(self):
        data = {'Date': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                'High': [50, 55, 53, 56, 52, 58, 54, 59, 50],
                'Low': [45, 48, 47, 49, 46, 49, 52, 51, 45]}
        df = pd.DataFrame(data)
        support_levels, resistance_levels = find_support_resistance_levels(df)
        
        # Expected support and resistance levels
        expected_support = [(6, 52), (8, 45)]
        expected_resistance = [(1, 55), (3, 56), (5, 58), (7, 59)]
        
        self.assertEqual(support_levels, expected_support)
        self.assertEqual(resistance_levels, expected_resistance)

if __name__ == '__main__':
    unittest.main()
