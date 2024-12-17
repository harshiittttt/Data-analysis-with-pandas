import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import yfinance as yf


def show_historical_price(ticker,startdate,enddate):
    data = yf.download(ticker,start=startdate,end=enddate)
    if data.empty:
        print("No data available")



    data = data.dropna()

   # monthly_average = data.groupby("Month")["Close"].mean()
    #print(monthly_average)
    return data.head(100)

def return_monthly_average_close(data):
    data["Month"] = pd.to_datetime(data.index).month
    monthly_average_close = data.groupby("Month")["Close"].mean()
    return monthly_average_close

def historical_price_analysis(data):


    return data.describe()

def main():


    user_ticker= input("please enter nasdaq symbol of the stock you want to visualize :: ").upper()
    no_of_days = int(input("For how many previous days you want to get the data :: "))
    yesterday = date.today() - timedelta(days=1)
    start = yesterday-timedelta(days=no_of_days)
    print(f"fetching data form {start} to {yesterday}")
    fetched_data = show_historical_price(user_ticker,start,yesterday)
    print(fetched_data)
    print("this is the latest data available with us")
    data_analysis = historical_price_analysis(fetched_data)
    print("MATHEMATICAL ANALYSIS AS FOLLOWS ::")
    print(data_analysis)
    print("Monthly averages close ::")
    monthly_average_close = return_monthly_average_close(fetched_data)
    monthly_average_close.reset_index()
    print(monthly_average_close)
    # Plot stock closing prices
    plt.figure(figsize=(10, 5))
    plt.plot(fetched_data.index, fetched_data["Close"], label="Closing Price")
    plt.title("Stock Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()




if __name__ == '__main__':
    main()