import pandas as pd
import pytest
import sys
sys.path.append(r'C:\Users\LUV\T')
from Algorithm_Functions import find_support_resistance_levels 

@pytest.fixture
def empty_dataframe():
    return pd.DataFrame()

@pytest.fixture
def data_no_support_resistance():
    data = {'Date': [1, 2, 3, 4, 5],
            'High': [50, 55, 53, 56, 52],
            'Low': [45, 48, 47, 49, 46]}
    return pd.DataFrame(data)

@pytest.fixture
def data_with_support_resistance():
    data = {'Date': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'High': [50, 55, 53, 56, 52, 58, 54, 59, 50],
            'Low': [45, 48, 47, 49, 46, 49, 52, 51, 45]}
    return pd.DataFrame(data)

def test_empty_dataframe(empty_dataframe):
    support_levels, resistance_levels = find_support_resistance_levels(empty_dataframe)
    assert support_levels == []
    assert resistance_levels == []

def test_no_support_or_resistance(data_no_support_resistance):
    support_levels, resistance_levels = find_support_resistance_levels(data_no_support_resistance)
    assert support_levels == []
    assert resistance_levels == []

def test_support_and_resistance_levels(data_with_support_resistance):
    support_levels, resistance_levels = find_support_resistance_levels(data_with_support_resistance)
    
    # Expected support and resistance levels
    expected_support = [(6, 52), (8, 45)]
    expected_resistance = [(1, 55), (3, 56), (5, 58), (7, 59)]
    
    assert support_levels == expected_support
    assert resistance_levels == expected_resistance
