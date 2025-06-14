import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


ticker  = 'MSFT'
start = '2020-06-12'
end = '2025-06-12'
data = yf.download(ticker, start=start, end=end)
opens = data["Open"].values.tolist()
closes = data["Close"].values.tolist()
low = data["Low"].values.tolist()
high = data["High"].values.tolist()
 
initial_capital = 100000
cash = initial_capital
shares  = 0
position = 0
equity_curve = [cash]

w1 = .3
w2 = .1
w3 = .6
b = 0
moving_average_threshold = 20

def delta(x, n):

    today_range = high[x-1][0] - low[x-1][0]
    prev_range = high[x-1-n][0] - low[x-1-n][0]

    if prev_range == 0 or today_range == 0:
        return 0

    today_val = (((closes[x-1][0] - low[x-1][0]) - (high[x-1][0] - closes[x-1][0])) / today_range)
    prev_val = (((closes[x-1-n][0] - low[x-1-n][0]) - (high[x-1-n][0] - closes[x-1-n][0])) / prev_range)
    return today_val - prev_val


def sma(x, current_index, window):
    sum = 0
    if current_index < window:
        return 0
    for i in range(current_index - window, current_index):
        sum += x[i][0]
    moving_average = sum / window
    return moving_average

for i in range(9, len(opens)):
    alpha1 = np.log(opens[i-1][0] / closes[i-1][0])
    alpha2 = (-1 * delta(i, 9))
    alpha3 = -1 * (opens[i][0] - sma(opens, i, 50)) # 50 day moving average
    composite = w1 * alpha1 + w2 * alpha2 + alpha3 * w3 + b

    if composite > 0 and position == 0:
        shares = cash / opens[i][0]
        position = 1
        cash = 0
    elif composite <= 0 and position == 1:
        cash = shares * opens[i][0]
        shares = 0
        position = 0
        
    port_value = cash + shares * closes[i][0]

    equity_curve.append(port_value)


plt.plot(equity_curve)
plt.show()
print(((cash - initial_capital) / initial_capital)*100)
print(((opens[-1][0] - opens[0][0])/ opens[0][0]) * 100)


