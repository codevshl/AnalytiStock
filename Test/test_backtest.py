import unittest
import pandas as pd
import sys
sys.path.append(r'C:\Users\LUV\T')
from Algorithm_Functions import calculate_profit

class TestStrategyFunctions(unittest.TestCase):
    
    def test_calculate_profit(self):
        # Test case 1: Buy and sell once with a profit
        data_case1 = pd.DataFrame({
            'Close': [100, 105, 110, 115, 120],
            'Signal': [0, 0, 1, -1, 0]
        })
        investment1, total_profit1, percentage_return1 = calculate_profit(data_case1)
        self.assertEqual(investment1, 110)
        self.assertEqual(total_profit1, 5)
        self.assertEqual(percentage_return1, 4.545)
        
        # Test case 2: Buy and sell once with a loss
        data_case2 = pd.DataFrame({
            'Close': [100, 95, 90, 85, 80],
            'Signal': [0, 0, 1, -1, 0]
        })
        investment2, total_profit2, percentage_return2 = calculate_profit(data_case2)
        self.assertEqual(investment2, 90)
        self.assertEqual(total_profit2, -5)
        self.assertEqual(percentage_return2, -5.556)
        
        # Test case 3: No trades, should return 0 values
        data_case3 = pd.DataFrame({
            'Close': [100, 105, 110, 115, 120],
            'Signal': [0, 0, 0, 0, 0]
        })
        investment3, total_profit3, percentage_return3 = calculate_profit(data_case3)
        self.assertEqual(investment3, 0)
        self.assertEqual(total_profit3, 0)
        self.assertEqual(percentage_return3, 0)
        
        
if __name__ == '__main__':
    unittest.main()
