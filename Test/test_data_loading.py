import unittest
import sys
sys.path.append(r'C:\Users\LUV\T')  # Add the path to the 'a' directory

# import yfinance as yf

# def load_data(ticker, start_date, end_date):
#     tickerSymbol = ticker
#     tickerData = yf.Ticker(tickerSymbol)
#     df = tickerData.history(period="1d", start=start_date, end=end_date)
#     return df

# %run -i dl.py load_data
from Algorithm_Functions import load_data

class TestDataLoading(unittest.TestCase):
    
    def test_invalid_date_range_empty_df(self):
        # Test loading data with an invalid date range
        ticker = "AAPL"  # Replace with a valid ticker symbol
        start_date = "2022-01-20"  # Invalid start date (after end_date)
        end_date = "2022-01-10"  # Invalid end date (before start_date)

        df = load_data(ticker, start_date, end_date)

        self.assertTrue(df.empty, f"Expected an empty DataFrame for invalid date range, but got a DataFrame with shape {df.shape}")
        
    def test_invalid_ticker_empty_df(self):
        # Test loading data with an invalid ticker symbol
        ticker = "INVALID"  # Replace with an invalid ticker symbol
        start_date = "2022-01-01"
        end_date = "2022-01-10"

        df = load_data(ticker, start_date, end_date)

        self.assertTrue(df.empty, f"Expected an empty DataFrame for invalid ticker, but got a DataFrame with shape {df.shape}")
        
    def test_valid_data_not_empty_df(self):
        # Test loading data with a valid ticker symbol and date range
        ticker = "AAPL"  # Replace with a valid ticker symbol
        start_date = "2022-01-01"
        end_date = "2022-01-10"

        df = load_data(ticker, start_date, end_date)

        self.assertFalse(df.empty, f"Expected a non-empty DataFrame for valid data, but got an empty DataFrame")


if __name__ == "__main__":
    unittest.main()
