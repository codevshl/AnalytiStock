# Trend_Finder_Updated

This is a program that allows the user to input a stock symbol, start date, and end date, and then loads the historical data for the specified period. The program then applies technical analysis indicators to the data, including RSI, simple moving averages, support and resistance levels, and a trading strategy based on the SMA20 and SMA50 crossover and the support and resistance levels. The program then returns the processed data and the investment and profit/loss from the trading strategy.

The program is implemented using the Tkinter library for the graphical user interface (GUI), Pandas for data processing, Matplotlib and mplfinance for visualization, TALib for technical analysis, and Yahoo Finance API for data retrieval.

The program consists of a load_data() function that takes three arguments: the stock symbol, start date, and end date. This function retrieves the historical data using the Yahoo Finance API and applies various technical indicators to the data. It then implements a simple trading strategy based on the SMA20 and SMA50 crossover and the support and resistance levels. The function returns the processed data and the investment and profit/loss from the trading strategy.

The program also includes a GUI that allows the user to input the stock symbol, start date, and end date, and then displays the processed data and the investment and profit/loss from the trading strategy. The GUI is implemented using Tkinter and includes input fields for the stock symbol, start date, and end date, as well as buttons to load the data and display the results.
