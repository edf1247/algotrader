import yfinance as yf
import sys


if __name__ == "__main__":
    try:
        ticker = sys.argv[1]
        start = sys.argv[2]
        end = sys.argv[3]
    except:
        print("Usage: python fetch_data.py <ticker> <start date> <end date>")
        sys.exit()

    data = yf.download(ticker, start=start, end=end)

    with open(f"stock_data/{ticker}-{start}-{end}.csv", "w") as file:
        file.write(data.to_string())
    
    print(f"Data written to stock_data/{ticker}-{start}-{end}.csv")
