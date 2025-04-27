!pip install fyers-apiv3> nul 2>&1

api = "NKSZ6X73S-100,PYJ39IZXM,https://www.google.com/"
app_id, secret_key, redirect_uri = api.split(',')
#Request Parameters for Step 1
# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Replace these values with your actual API credentials
# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=app_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type = "code"
)

# Generate the auth code using the session model
response = session.generate_authcode()

# Print the auth code received in the response
print("https://trade.fyers.in")
print(response)

#Request Parameters for Step 2
# The authorization code received from Fyers after the user grants access
auth_code=input("").replace('https://www.google.com/?s=ok&code=200&auth_code=', '').replace("&state=None","")

# Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=app_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type = "code",
    grant_type = "authorization_code"
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
print(response)
# STEP 5: Save to Excel
import pandas as pd
if isinstance(response, dict):
    daf = pd.DataFrame([response])  # Wrap in list to create a single-row dataframe
    daf=daf[['access_token','code','message']]
    daf['access_token']=app_id+":"+daf['access_token']
    daf.to_excel("fyers_token_response.xlsx", index=False)





#Download the file
from google.colab import files
files.download("fyers_token_response.xlsx")


