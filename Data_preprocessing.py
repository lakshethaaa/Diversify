import numpy as np
import pandas as pd
import plotly as plt
import yfinance as yf

# Stocks

uber = yf.download(tickers = 'UBER', period = '1y', interval = '1d')
uber['Identifier'] = 'Uber'

uber['Moving_Average'] = uber['Close'].rolling(window=30).mean()
#Calculate the percentage return based on the moving average
uber['Moving_Average_Percentage_Return'] = math.abs(uber['Close'] - uber['Moving_Average']) / uber['Moving_Average'] * 100

amazon = yf.download(tickers = 'AMZN', period = '1y', interval = '1d')
amazon['Identifier'] = 'Amazon'

amazon['Moving_Average'] = amazon['Close'].rolling(window=30).mean()
#Calculate the percentage return based on the moving average
amazon['Moving_Average_Percentage_Return'] = math.abs(amazon['Close'] - amazon['Moving_Average']) / amazon['Moving_Average'] * 100

tesla = yf.download(tickers = 'TSLA', period = '1y', interval = '1d')
tesla['Identifier'] = 'Tesla'

tesla['Moving_Average'] = tesla['Close'].rolling(window=30).mean()
#Calculate the percentage return based on the moving average
tesla['Moving_Average_Percentage_Return'] = math.abs(tesla['Close'] - tesla['Moving_Average']) / tesla['Moving_Average'] * 100

apple = yf.download(tickers = 'APPL', period = '1y', interval = '1d')
apple['Identifier'] = 'Apple'

apple['Moving_Average'] = apple['Close'].rolling(window=30).mean()
#Calculate the percentage return based on the moving average
apple['Moving_Average_Percentage_Return'] = math.abs(apple['Close'] - apple['Moving_Average']) / apple['Moving_Average'] * 100

meta = yf.download(tickers = 'META', period = '1y', interval = '1d')
meta['Identifier'] = 'Meta'

meta['Moving_Average'] = meta['Close'].rolling(window=30).mean()
#Calculate the percentage return based on the moving average
meta['Moving_Average_Percentage_Return'] = math.abs(meta['Close'] - meta['Moving_Average']) / meta['Moving_Average'] * 100

# Drop the first 50 columns which are lost because of moving average
uber = uber.iloc[50:]
meta = meta.iloc[50:]
tesla = tesla.iloc[50:]
apple = apple.iloc[50:]
amazon = amazon.iloc[50:]

df1 = pd.concat([uber,amazon,tesla,apple,meta])
df1 = df1.drop(columns= ['Moving_Average'])

df2 = yf.download(tickers = 'GC=F',period= '1y')

df2['Moving_Average'] = df2['Close'].rolling(window=30).mean()
# Calculate the percentage return based on the moving average
df2['Moving_Average_Percentage_Return'] = (df2['Close'] - df2['Moving_Average']) / df2['Moving_Average'] * 100

# Drop the Moving average column 
df2 = df2.iloc[50:]
df2 = df2.drop(columns = 'Moving_Average')

df3 = yf.download(tickers = 'REIT',period= '1y')

df3['Moving_Average'] = df3['Close'].rolling(window=30).mean()
# Calculate the percentage return based on the moving average
df3['Moving_Average_Percentage_Return'] = (df3['Close'] - df3['Moving_Average']) / df3['Moving_Average'] * 100

df3 = df3.iloc[50:]
df3 = df3.drop(columns='Moving_Average')

