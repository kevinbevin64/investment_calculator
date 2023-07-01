import yfinance as yf
from datetime import datetime, timedelta

def last_date(day_name):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    current_date = datetime.today()
    current_day_number = current_date.weekday()

    target_day_number = days.index(day_name)
    date_difference = (7 + current_day_number - target_day_number) % 7
    if date_difference == 0: 
        date_difference = 7

    target_date = current_date - timedelta(days=date_difference)
    return target_date

def date_only(date):
    # Convert datetime object into YYYY-MM-DD form
    return date.strftime("%Y-%m-%d")

def date_ago(number_of_days, from_date):
    return from_date - timedelta(days=number_of_days)

def stock_price_on(date, stock_name):
    try: 
        data = yf.download(stock_name, start=date_only(date), end=date_only(date + timedelta(days=1)), progress=False)
    except:
        data = yf.download(stock_name, start=date_only(date - timedelta(days=1)), end=date_only(date + timedelta(days=0)), progress=False)
    return data["Close"]


if __name__ == '__main__':
    # print(stock_price_on(datetime("2023-04-06"), "AAPL"))




    # stock_name = input("Enter the stock name: ").upper()
    # scalar = float(input("Apple's scalar should be 1, Tesla's should be 0.25. \nEnter the scalar: "))
    # three_months_ago = date_ago(84, last_date("Friday"))
    # one_month_ago = date_ago(28, last_date("Friday"))
    # one_week_ago = date_ago(7, last_date("Friday"))
    # most_recent = last_date("Friday")
    # print(f"Last Friday: {date_only(most_recent)}")
    # current_stock_price = stock_price_on(most_recent, stock_name)
    # weights = (10, 20, 30)
    # weight_total = weights[0] + weights[1] + weights[2]
    # S = (weights[0] * ((current_stock_price / stock_price_on(three_months_ago, stock_name) - 1) * 100)
    #     + weights[1] * ((current_stock_price / stock_price_on(one_month_ago, stock_name) - 1) * 100)
    #     + weights[2] * ((current_stock_price / stock_price_on(one_week_ago, stock_name) - 1) * 100)) / weight_total
    # print(f"{S = }\n")
    # print("Amount to invest = $", end="")
    # if S < 0: 
    #     print(round(scalar * (100 - 8 * S), 2))
    # else: 
    #     print(round(scalar * (100 + 2 * S), 2))

   



