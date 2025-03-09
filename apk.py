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


#Download the file
from google.colab import files
files.download(file)

print(option)














api=""#client_id,client_secret,redirect_uri

#!pip install requests
#!pip install pandas

import requests
import pandas as pd

# Define parameters
client_id = api.split(',')[0]# Replace with your client ID
client_secret = api.split(',')[1]# Replace with your secret key
redirect_uri = api.split(',')[2] # Replace with your redirect URI
state = ''

# Construct the authorization URL
authorization_url = (
    f"https://api.upstox.com/v2/login/authorization/dialog?"
    f"client_id={client_id}&redirect_uri={redirect_uri}&state={state}"
)
print("Visit this URL to authorize the application:", authorization_url)
# Simulating user authorization and retrieving the authorization code from the redirected URL
google_url = input('URL received after redirection: ')
auth_code = google_url.split("code=")[-1]

# Define the URL for the API endpoint to exchange the auth code for a token
token_url = 'https://api.upstox.com/v2/login/authorization/token'

# Set the headers for the token request
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Prepare the data payload for the token request
data = {
    'code': auth_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'grant_type': 'authorization_code'
}

# Make the POST request to get the token
response = requests.post(token_url, headers=headers, data=data)
if response.status_code == 200:
    access_token = response.json().get("access_token")
    print("Access Token:", access_token)

# Check if access_token was retrieved
if access_token:
    # Create a DataFrame to store the access token
    df = pd.DataFrame({'app_name':'upstox','access_token': [access_token]})

    # Save the DataFrame to an Excel file
    df.to_excel('upstox_token.xlsx', index=False)


#Download the file
from google.colab import files
files.download("upstox_token.xlsx")
