date = input("")#04032025
bhavcopy = f"https://nsearchives.nseindia.com/archives/nsccl/volt/FOVOLT_{date}.csv"
print(bhavcopy)



from datetime import datetime
import pytz

# Set the timezone (e.g., 'Asia/Kolkata' for Indian Standard Time)
timezone = pytz.timezone('Asia/Kolkata')

# Get the current date and time in the specified timezone
current_date = datetime.now(timezone)

# Format the date as mmmyyyy in lowercase (e.g., feb2025)
formatted_date = current_date.strftime("%b%Y").lower()
# Corrected print statement
fno_stock= f"https://nsearchives.nseindia.com/content/nsccl/mpl_{formatted_date}.csv"




import requests
import pandas as pd

# Step 1: Download the Nifty 500 list
headers = {'User-Agent': 'Mozilla/5.0'}

# Download the CSV
response = requests.get(fno_stock, headers=headers)
if response.status_code == 200:
    # Load the content into a DataFrame directly without saving it as a file
    from io import StringIO
    data = pd.read_csv(StringIO(response.content.decode('utf-8')))
    data.rename(columns={'UNDERLYING_NAME': 'Symbol'}, inplace=True)



    # Step 2: Create Yahoo Finance ticker symbols

    data['segment']="NFO-OPT"
    data=data[['Symbol','segment']]
    data['yahoo']=data['Symbol']+".NS"
    #data['fyers'] = "'NSE:"+data['Symbol'] + "-EQ',"

    #print(data)











import requests
import pandas as pd

# Step 1: Download the Nifty 500 list
headers = {'User-Agent': 'Mozilla/5.0'}

# Download the CSV
response = requests.get(bhavcopy, headers=headers)
if response.status_code == 200:
    # Load the content into a DataFrame directly without saving it as a file
    from io import StringIO
    bhav_data = pd.read_csv(StringIO(response.content.decode('utf-8')))
    bhav_data.rename(columns={' Underlying Close Price (A)': 'Prev.Close'}, inplace=True)
    #print(bhav_data)



# Filter for options in the specified segments
bhav_data = bhav_data[(bhav_data[' Symbol'].isin(data['Symbol']))].sort_values(by='Prev.Close')
bhav_data = bhav_data[(bhav_data['Prev.Close'] >= 1) & (bhav_data['Prev.Close'] <= 5000000)]

bhav_data=bhav_data[[' Symbol','Prev.Close']]
print(bhav_data)