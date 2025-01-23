import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf 

#want to predict stock price for S&P500

ticker = yf.Ticker("^GSPC") #set to SP500, but can change to whatever is desired

ticker = ticker.history(period = "max")


del ticker["Dividends"] #good for singular stocks
del ticker["Stock Splits"] #good for singular stocks

print (ticker)
print (ticker.index)

#print (ticker.plot.line(y="Close", use_index = "true"))



#want to know will stock go up or down tommorow
#ticker["Tommorow price"] = sp500["Close"].shift(-1)