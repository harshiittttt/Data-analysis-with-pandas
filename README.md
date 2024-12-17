# Data-analysis-with-pandas
# 📈 Stock Price Visualizer

**A Simple Python-based stock price visualization tool that fetches and analyzes historical stock data using the Yahoo Finance API, calculates monthly averages, and generates insightful visualizations.**  

---

## 🚀 Features
- 📊 **Fetch Stock Data**: Uses the Yahoo Finance API (`yfinance`) to retrieve historical stock prices.
- 🗓️ **Custom Date Range**: User specifies the number of previous days to fetch data.
- 📉 **Data Analysis**: Provides summary statistics like mean, standard deviation, and more.
- 📅 **Monthly Averages**: Calculates and displays monthly average closing prices.
- 📈 **Graphical Visualization**: Plots stock prices over time using `matplotlib`.

---

## 🛠️ Libraries Used  
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-ffb800?logo=plotly)
![YahooFinance](https://img.shields.io/badge/Yahoo%20Finance-API%20Integration-232F3E?logo=yahoo)

---

## 🖥️ Screenshots

### 📄 Fetched Data
![Fetched Data](images/data.PNG)

### 📊 Data Analysis
![Data Analysis](images/data_analysis.png)

### 📅 Monthly Average Close
![Monthly Average Close](images/monthly_average_close.png)

### 📈 Closing Price Graph
![Graph](images/graph.png)

---

## 📜 How It Works

1. The user provides:
   - The **stock ticker** (e.g., TSLA for Tesla).
   - The **number of previous days** to fetch the stock price data.
2. The program fetches data using the **Yahoo Finance API** (`yfinance`).
3. It performs:
   - Summary analysis of the data.
   - Calculation of **monthly average closing prices**.
4. It visualizes the **stock closing prices** on a graph.

---

## 🏗️ Code Structure

- **`show_historical_price()`**: Fetches stock data, drops any missing values, and displays the top records.
- **`return_monthly_average_close()`**: Calculates monthly average closing prices.
- **`historical_price_analysis()`**: Generates summary statistics of the stock data.
- **`main()`**: Orchestrates user inputs, data fetching, analysis, and visualization.

---

## 🧩 Requirements
To run this project, you need the following:

- **Python 3.8+**
- **Pandas**
- **Matplotlib**
- **yfinance**

### Install Dependencies
Run the following command to install the required libraries:
```bash
pip install pandas matplotlib yfinance
