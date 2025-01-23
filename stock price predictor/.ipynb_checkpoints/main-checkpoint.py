import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf 

#want to predict stock price for S&P500

sp500 = yf.Ticker("^GSPC")

sp500 = sp500.history(period = "max")

#print (sp500)
#print (sp500.index)

plt.figure(figsize=(15,5))
plt
sp500.plot.line(y="Close", use_index = "true")
