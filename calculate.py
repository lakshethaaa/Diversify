from sklearn.preprocessing import MinMaxScaler
def func_calculate_percentage_returns(string,num):
    df = yf.download(tickers = string ,period='1y',interval='1d')
    scaler = MinMaxScaler()
    numerical_cols = ['Open', 'Close', 'High', 'Low', 'Volume', 'Adj Close']
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Define your sequence length (e.g., number of past days to consider)
    sequence_length = 30

    # Create sequences of data
    X3 = []

    for i in range(len(df) - sequence_length):
        X3.append(df[numerical_cols].values[i:i+sequence_length])
        #y2.append(df['Moving_Average_Percentage_Return'].values[i+sequence_length])

    X3 = np.array(X3)
    if num == 1:
        x = model.predict(X3)
    elif num == 2:
        x = model1.predict(X3)
    else:
        x = model2.predict(X3)
    ans = 0
    for i in range(0,len(x)):
        ans += x[i]
    return ans/len(x)
def list_of_percentage_returns(string,string1,string2):
    ans = []
    ans.append(func_calculate_percentage_returns(string, 1))
    ans.append(func_calculate_percentage_returns(string1, 2))
    ans.append(func_calculate_percentage_returns(string2, 3))
    print(ans)
    allocation = 0
    # Calculate allocation weights based on predicted returns
    total_return = sum([x[0] for x in ans])
    allocation = [x[0] / total_return for x in ans]
    return allocation
