import yfinance as yf
import pandas as pd

def filter_data(name, segment, ticker):
    # Get stock data
    stock = yf.Ticker(ticker)
    current_price = stock.history(period='1d')['Close'].iloc[-1]

    # Round to the nearest 100
    rounded_price = round(current_price, -2).astype(int)

    df = pd.read_csv('https://api.kite.trade/instruments')
    df = df[(df['name'] == name) & (df['segment'] == segment)]
    current_expiry = df.iloc[0, 5]
    df = df[(df['expiry'] == current_expiry)]
    df = df[(df['strike'] >= rounded_price - 1000) &
            (df['strike'] <= rounded_price + 1000)].sort_values(by='strike')

    # Convert and format 'expiry' column in one line
    df['expiry'] = pd.to_datetime(df['expiry']).dt.strftime('%d-%m-%Y')
    df['strike']=df['strike'].astype(int)
    #watchlist
    df['zerodha'] = df['exchange'] + ":" + df['tradingsymbol']  
    
    # Now you can drop the 'exchange' column
    df = df.drop(columns=['tick_size', 'last_price']) 
    return df

# Filter NIFTY options
nifty_data = filter_data("NIFTY", "NFO-OPT", "^NSEI")
banknifty_data = filter_data("BANKNIFTY", "NFO-OPT", "^NSEBANK")
finnifty_data = filter_data("FINNIFTY", "NFO-OPT", "NIFTY_FIN_SERVICE.NS")
sensex_data = filter_data("SENSEX", "BFO-OPT", "^BSESN")
bankex_data = filter_data("BANKEX", "BFO-OPT", "BSE-BANK.BO")

# magic_codes
option = pd.concat([nifty_data, banknifty_data, finnifty_data, sensex_data, bankex_data], ignore_index=True)


file="option_trading.xlsx"
# Save combined data to a single CSV file
option.to_excel(file, index=False)

print(option)