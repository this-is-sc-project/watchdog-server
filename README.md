# Yahoo Finance News Crawler

## Overview

This project is a Python script that crawls news articles for specified stock tickers from Yahoo Finance and saves them to a CSV file. It uses Selenium to navigate web pages and extract news article titles, contents, and links.

## Features

* Crawls news articles from the Yahoo Finance news page for the specified stock tickers.
* Extracts article titles, contents, and links.
* Stores the extracted data in a Pandas DataFrame.
* Saves the DataFrame to a CSV file.
* Loads existing data, merges it with the newly crawled data, and removes duplicates.


## Usage

1. Install the required libraries: `selenium`, `pandas`.
2. Update the `path` variable to the desired directory for saving the CSV file.
3. Update the `tickers` list with the desired stock tickers.
4. Run the script.


## Code Explanation

### Load Existing Data
Use code with caution
python import pandas as pd
 
This code reads existing CSV files from the specified path and stores them in Pandas DataFrames. The DataFrames for each stock ticker are stored in the `dfs` dictionary.


### Add New News 
This code calls the `get_news` function to crawl new news articles for each stock ticker. The new data is merged with the existing DataFrame, and duplicate rows and missing values are removed. The final DataFrame is saved to a CSV file.


## Notes
* The `get_news` function uses Selenium to extract data from the Yahoo Finance news page. This function is defined in a separate file.
* This script is designed to run in the Google Colab environment. To run it in other environments, you may need to install the necessary libraries and modify the paths accordingly.
