#kite
import pandas as pd

def filter_data(name, segment):
    df = pd.read_csv('https://api.kite.trade/instruments')
    df = df[(df['name'] == name) & (df['segment'] == segment)]
    current_expiry = df.iloc[0, 5]
    df = df[(df['expiry'] == current_expiry)]
    # Convert the expiry column to datetime format
    df['expiry'] = pd.to_datetime(df['expiry'], errors='coerce')
    # Format the 'expiry' column as dd-mm-yyyy
    df['expiry'] = df['expiry'].dt.strftime('%d-%m-%Y')
    return df

# Filter NIFTY options
nifty_data = filter_data("NIFTY", "NFO-OPT")
banknifty_data = filter_data("BANKNIFTY", "NFO-OPT")
finnifty_data = filter_data("FINNIFTY", "NFO-OPT")

# Filter BANKEX options
sensex_data = filter_data("SENSEX", "BFO-OPT")
bankex_data = filter_data("BANKEX", "BFO-OPT")
crude_data = filter_data("CRUDEOIL", "MCX-OPT")
option = pd.concat([nifty_data,banknifty_data,finnifty_data,sensex_data,bankex_data], ignore_index=True)
# Remove columns 'tick_size' and 'last_price'
option = option.drop(columns=['tick_size', 'last_price','instrument_token'])

print(option)