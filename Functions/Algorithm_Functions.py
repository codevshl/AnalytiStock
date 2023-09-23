import sys
sys.path.append(r'C:\Users\LUV\T')
from Chart_visualisation_functions import load_data,find_support_resistance_levels,filter_support_resistance_levels

import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf
import talib as tb
import matplotlib.dates as mdates

def calculate_technical_indicators(df):
    df['SMA20'] = tb.SMA(df['Close'], timeperiod=20)
    df['SMA50'] = tb.SMA(df['Close'], timeperiod=50)
    df['RSI'] = tb.RSI(df['Close'].values, timeperiod=14)
    return df

def add_support_resistance_columns(df, updated_support_levels, updated_resistance_levels):
    df['Resistance'] = 0
    df['Support'] = 0

    for index, row in df.iterrows():
        high_value = row['High']
        if any(high_value == url[1] for url in updated_resistance_levels):
            df.at[index, 'Resistance'] = 1

        low_value = row['Low']
        if any(low_value == usl[1] for usl in updated_support_levels):
            df.at[index,'Support'] = 1
    return df

def generate_signals(df):
    df['Signal'] = np.where((df['SMA20'] > df['SMA50'])  & (df['Support'] == 1), 1, np.where((df['SMA20'] < df['SMA50']) & (df['Resistance'] == 1), -1, 0))
    
#     df[df['Signal'] == 1]
#     df[df['Signal'] == -1]
    df = df.reset_index(drop=True)
    return df

def calculate_profit(df):
    positions = []
    profit = []
    investment = 0

    for i, row in df.iterrows():
        if row['Signal'] == 1:
            buy_price = df.loc[i+1, 'Open']
            positions.append({'buy_price': buy_price})
        elif row['Signal'] == -1:
            if len(positions) > 0:
                for pos in positions:
                    investment += pos['buy_price']
                    profit.append(row['Close'] - pos['buy_price'])
                positions = []
    percentage_return = (sum(profit) / investment) * 100 if investment > 0 else 0           

    return investment, sum(profit), percentage_return

# Example usage
def main_function(ticker = "AAPL",start_date = "2020-01-01",end_date = "2022-12-31"):

    data = load_data(ticker, start_date, end_date)
    data = calculate_technical_indicators(data)
    support_levels, resistance_levels = find_support_resistance_levels(data)
    updated_support_levels, updated_resistance_levels = filter_support_resistance_levels(data, support_levels, resistance_levels)
    data = add_support_resistance_columns(data, updated_support_levels, updated_resistance_levels)
    data = generate_signals(data)
    investment, total_profit, percentage_return=calculate_profit(data)
    return data,investment, total_profit, percentage_return

