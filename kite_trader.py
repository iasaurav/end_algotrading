import pandas as pd

def filter_data(name, segment):

    df = pd.read_csv('https://api.kite.trade/instruments')
# Filtering the required segments
    
    df = df[df["segment"].isin(["NFO-OPT", "BFO-OPT", "MCX-OPT"])]
    
    
    df['strike']=df['strike'].astype(int)
    df = df[(df['name'] == name) & (df['segment'] == segment)]
    current_expiry = df.iloc[0, 5]
    df = df[(df['expiry'] == current_expiry)]

    # Convert and format 'expiry' column in one line
    df['expiry'] = pd.to_datetime(df['expiry']).dt.strftime('%d-%m-%Y')


    
    return df

# Filter NIFTY options
nifty_data = filter_data("NIFTY", "NFO-OPT")
banknifty_data = filter_data("BANKNIFTY", "NFO-OPT")
finnifty_data = filter_data("FINNIFTY", "NFO-OPT")
sensex_data = filter_data("SENSEX", "BFO-OPT")
bankex_data = filter_data("BANKEX", "BFO-OPT")

# basic_codes
option = pd.concat([nifty_data, banknifty_data, finnifty_data, sensex_data, bankex_data], ignore_index=True)


# Save combined data to a single CSV file
option.to_excel("current_trading.xlsx", index=False)

print(option)


#Download the file
from google.colab import files
files.download("current_trading.xlsx")
