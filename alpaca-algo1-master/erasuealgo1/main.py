from portfolio_mananger import PortfolioManager
from get_tickers import stocks_to_long, stocks_to_short
import erasure
import time

erasure.main()

manager = PortfolioManager()


for sym in stocks_to_long():
    manager.add_items([[sym, 0.05]])

for sym in stocks_to_short():
    manager.add_items([[sym, -0.05]])

manager.format_percent(0.05)
manager.percent_rebalance('block')
time.sleep(86399)





