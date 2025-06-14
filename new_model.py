import backtrader as bt

if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.00)
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue():.2f}")
    cerebro.run()
    print(f"Ending Portfolio Value: {cerebro.broker.getvalue():.2f}")