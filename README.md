# Trend Finder

![Project Image](project_image.png)

This is a Python program for analyzing stock data using various technical indicators and implementing a simple trading strategy. The program allows the user to input a stock symbol, start date, and end date, then loads historical data for the specified period, applies technical analysis indicators, and provides investment and profit/loss information based on a trading strategy.


## Features

- Retrieve historical stock data using Yahoo Finance API.
- Candlestick Chart visualization of support and resistance levels.
- Apply technical analysis indicators, including RSI, simple moving averages, support and resistance levels.
- Implement a trading strategy based on the SMA20 and SMA50 crossover and support/resistance levels.
- GUI implemented using Tkinter for user-friendly interaction.


## Update 1

- Unit testing using `unittest` and `pytest`.
- Code coverage analysis.
- Exception handling.
- File handling.
- Backtesting algorithm on multiple stocks and time ranges.
- Cleaned candlestick chart visualization.
- Advanced trading algorithm utilizing multiple indicators.
- Enhanced user-friendly GUI with additional charts.
- Improved code and file structure


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/codevshl/Trend_Finder_Updated.git


## Usage
Run the main program:
- Run GUI file using required commands

- The GUI will open, allowing you to input the stock symbol, start date, and end date.

- Click the ` Submit ` button to retrieve and analyze the stock data.

- It will display the processed data and investment/profit information.

- Click the ` Display Dataframe ` button for get data of ticker symbol you provided

- Click on dropdown button and click on ` Plot Data ` to get required charts


## Testing
1. For unittest:

```bash
cd "required_path"
python "your_filename"
```
Replace your_test_directory/ with the actual directory where your test files are located and your_filename with the actual filename.

2. For pytest:

If you haven't already installed pytest, you can do so using pip:

```bash
pip install pytest
```

```bash
cd "required_path"
pytest "your_filename"
```
Replace your_test_directory/ with the actual directory where your test files are located and your_filename with the actual filename.


## Code Coverage

1. Install coverage.py:

If you haven't already installed coverage.py, you can do so using pip:

```bash
pip install coverage
```
Run coverage.py with pytest or unittest:

Use coverage.py to run your tests and collect coverage data. You can execute the following command:

``` bash
coverage run -m pytest/unittest your_test_directory/
```
Replace your_test_directory/ with the actual directory where your test files are located and choose pytest or unittest accordingly.

2. Generate Coverage Report:

After running the tests, you can generate a coverage report by running:

```bash
coverage report -m
```
This command will display the code coverage report in the terminal, including the percentage of code coverage achieved for each module and function.

