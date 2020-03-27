import pandas as pd
from pandas import DataFrame
import numpy as np


def stocks_to_long():
    tickers = pd.read_csv('stocks_to_trade').tail(10)
    df = DataFrame(tickers, columns=['symbol', 'score'])
    stock = df["symbol"].to_list()
    return stock


def stocks_to_short():
    tickers = pd.read_csv('stocks_to_trade').head(10)
    df = DataFrame(tickers, columns=['symbol', 'score'])
    stock = df["symbol"].to_list()
    return stock

