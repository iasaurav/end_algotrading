import pandas as pd
# Read data from URL
url = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"
data = pd.read_csv(url).iloc[:, :15]
# Define filter conditions
conditions = (
    ((data['UNDERLYING_SYMBOL'] == 'NIFTY') & (data['EXCH_ID'] == 'NSE') & (data['SEGMENT'] == 'D') & (data['INSTRUMENT'] == 'OPTIDX')) |
    ((data['UNDERLYING_SYMBOL'] == 'BANKNIFTY') & (data['EXCH_ID'] == 'NSE') & (data['SEGMENT'] == 'D') & (data['INSTRUMENT'] == 'OPTIDX')) |
    ((data['UNDERLYING_SYMBOL'] == 'FINNIFTY') & (data['EXCH_ID'] == 'NSE') & (data['SEGMENT'] == 'D') & (data['INSTRUMENT'] == 'OPTIDX')) |
    ((data['UNDERLYING_SYMBOL'] == 'SENSEX') & (data['EXCH_ID'] == 'BSE') & (data['SEGMENT'] == 'D') & (data['INSTRUMENT'] == 'OPTIDX')) |
    ((data['UNDERLYING_SYMBOL'] == 'BANKEX') & (data['EXCH_ID'] == 'BSE') & (data['SEGMENT'] == 'D') & (data['INSTRUMENT'] == 'OPTIDX')) |
    ((data['UNDERLYING_SYMBOL'] == 'CRUDEOIL') & (data['EXCH_ID'] == 'MCX') & (data['SEGMENT'] == 'M') & (data['INSTRUMENT'] == 'OPTFUT'))
)

# Apply filter
data = data[conditions]


print(data)