# import PyQt5
# %matplotlib qt5

import numpy as np
import pandas as pd
import yfinance as yf
import mpl_finance as mpf
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from IPython.display import Image
import talib

def load_data(ticker, start_date, end_date):
    tickerSymbol = ticker
    tickerData = yf.Ticker(tickerSymbol)
    df = tickerData.history(period="1d", start=start_date, end=end_date)
    df['Date'] = mdates.date2num(df.index)
    
     # Check if the DataFrame is empty, return it immediately if it is
    if df.empty:
        return df
    
    # Check if the columns exist before dropping them
    columns_to_drop = ['Stock Splits', 'Dividends']
    existing_columns = df.columns.tolist()
    for column in columns_to_drop:
        if column in existing_columns:
            df.drop(column, axis=1, inplace=True)
    
    return df

def plot_candlestick_chart(df, save_filename=None):
    plt.rcParams['figure.figsize'] = [12, 12]
    plt.rc('font', size=14)
    fig, ax = plt.subplots()
    mpf.candlestick_ohlc(ax, df[['Date', 'Open', 'High', 'Low', 'Close']].values,
                         width=0.8, colorup='green', colordown='red')
    date_format = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    ax.set_title('Candlestick Chart')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price ($)')

    if save_filename:
        fig.savefig(save_filename)
    else:
        plt.show()

# Define functions for support and resistance
def isSupport(df, i):
    support = (
        df['Low'][i] < df['Low'][i - 1]
        and df['Low'][i] < df['Low'][i + 1]
        and df['Low'][i + 1] < df['Low'][i + 2]
        and df['Low'][i - 1] < df['Low'][i - 2]
    )
    return support

def isResistance(df, i):
    resistance = (
        df['High'][i] > df['High'][i - 1]
        and df['High'][i] > df['High'][i + 1]
        and df['High'][i + 1] > df['High'][i + 2]
        and df['High'][i - 1] > df['High'][i - 2]
    )
    return resistance

# Find and store support and resistance levels
def find_support_resistance_levels(df):
    resistance_levels = []
    support_levels = []

    for i in range(2, df.shape[0]-2):
        if isSupport(df, i):
            support_levels.append((i, df['Low'][i]))
        elif isResistance(df, i):
            resistance_levels.append((i, df['High'][i]))

    return support_levels, resistance_levels

def plot_support_resistance_chart(df, levels, levelr, save_filename='sup_res.png'):
    fig, ax = plt.subplots()
    mpf.candlestick_ohlc(ax, df[['Date', 'Open', 'High', 'Low', 'Close']].values, width=0.8, colorup='green', colordown='red', alpha=0.8)
    date_format = mdates.DateFormatter('%d %b %Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    ax.set_title('Support/Resistance Candlestick Chart', color='#800080', bbox=dict(facecolor='lightgrey', edgecolor='black'))
    ax.set_xlabel('Date', color='#800080')
    ax.set_ylabel('Price ($)', color='#800080')
    fig.tight_layout()

    support_label = 'Support'
    resistance_label = 'Resistance'

    support_lines = []
    for level in levels:
        line = plt.hlines(level[1], xmin=df['Date'][level[0]], xmax=max(df['Date']), colors='blue', label=support_label)
        support_lines.append(line)

    resistance_lines = []
    for level in levelr:
        line = plt.hlines(level[1], xmin=df['Date'][level[0]], xmax=max(df['Date']), colors='#DEC20B', label=resistance_label)
        resistance_lines.append(line)

    legend_lines = [Line2D([0], [0], color='blue', lw=2, label=support_label), Line2D([0], [0], color='#DEC20B', lw=2, label=resistance_label)]
    ax.legend(handles=legend_lines, facecolor='lightgrey', framealpha=1.0)
    fig.savefig(save_filename)
    plt.show()

 

def plot_support_resistance_chart(df, levels, levelr, save_filename='sup_res.png'):
    fig, ax = plt.subplots()
    mpf.candlestick_ohlc(ax, df[['Date', 'Open', 'High', 'Low', 'Close']].values, width=0.8, colorup='green', colordown='red', alpha=0.8)
    date_format = mdates.DateFormatter('%d %b %Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    ax.set_title('Support/Resistance Candlestick Chart', color='#800080', bbox=dict(facecolor='lightgrey', edgecolor='black'))
    ax.set_xlabel('Date', color='#800080')
    ax.set_ylabel('Price ($)', color='#800080')
    fig.tight_layout()

    support_label = 'Support'
    resistance_label = 'Resistance'

    support_lines = []
    for level in levels:
        line = plt.hlines(level[1], xmin=df['Date'][level[0]], xmax=max(df['Date']), colors='blue', label=support_label)
        support_lines.append(line)

    resistance_lines = []
    for level in levelr:
        line = plt.hlines(level[1], xmin=df['Date'][level[0]], xmax=max(df['Date']), colors='#DEC20B', label=resistance_label)
        resistance_lines.append(line)

    legend_lines = [Line2D([0], [0], color='blue', lw=2, label=support_label), Line2D([0], [0], color='#DEC20B', lw=2, label=resistance_label)]
    ax.legend(handles=legend_lines, facecolor='lightgrey', framealpha=1.0)
    fig.savefig(save_filename)
    plt.show()

 

   
def filter_support_resistance_levels(df, support_levels, resistance_levels):
    avg_candlesize = np.mean(df['High'] - df['Low'])
    
    updated_support_levels = []
    updated_resistance_levels = []

    for i in range(2,df.shape[0]-2):
        
        if isSupport(df,i):
          l = df['Low'][i]
          if isFarFromLevel(l,avg_candlesize, updated_support_levels, updated_resistance_levels):
            updated_support_levels.append((i,l))
        elif isResistance(df,i):
          l = df['High'][i]
          if isFarFromLevel(l,avg_candlesize, updated_support_levels, updated_resistance_levels):
            updated_resistance_levels.append((i,l))
            
    return updated_support_levels, updated_resistance_levels

def isFarFromLevel(l, avg_candlesize, updated_support_levels, updated_resistance_levels):
    
    # check if l is far from support levels
    far_from_support = np.sum([abs(l-x[1]) < avg_candlesize for x in updated_support_levels]) == 0
    # check if l is far from resistance levels
    far_from_resistance = np.sum([abs(l-x[1]) < avg_candlesize for x in updated_resistance_levels]) == 0
             
    return far_from_support or far_from_resistance

def main():
    ticker_symbol = 'AAPL'
    start_date = '2022-03-08'
    end_date = '2023-03-08'

    df = fetch_stock_data(ticker_symbol, start_date, end_date)
    calculate_technical_indicators(df)
    plot_candlestick_chart(df, 'candlestick_chart.png')
    
    support_levels, resistance_levels=find_support_resistance_levels(df)
    plot_support_resistance_chart(df, support_levels, resistance_levels, save_filename='noisy_sup_res.png')
    
    updated_support_levels, updated_resistance_levels = filter_support_resistance_levels(df,  support_levels, resistance_levels)
    plot_support_resistance_chart(df,updated_support_levels, updated_resistance_levels, save_filename='clean_sup_res.png')


if __name__ == "__main__":
    main()