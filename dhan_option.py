import warnings
warnings.filterwarnings("ignore")  # This will suppress all warnings.


import pandas as pd

def filter_data(name,exchange,segment,instrument):
    df = pd.read_csv('https://images.dhan.co/api-data/api-scrip-master-detailed.csv')
    df = df[(df['UNDERLYING_SYMBOL'] == name) &(df['EXCH_ID'] == exchange) & (df['SEGMENT'] == segment)&(df['INSTRUMENT'] == instrument) ]
    return df

# Filter options
nifty_data = filter_data("NIFTY", "NSE","D","OPTIDX")
banknifty_data = filter_data("BANKNIFTY", "NSE","D","OPTIDX")
finnifty_data = filter_data("FINNIFTY", "NSE","D","OPTIDX")
sensex_data = filter_data("SENSEX", "BSE","D","OPTIDX")
bankex_data = filter_data("BANKEX", "BSE","D","OPTIDX")

option = pd.concat([nifty_data,banknifty_data,finnifty_data,sensex_data,bankex_data], ignore_index=True)


print(option)

option.to_excel('dhan_option.xlsx', index=False)