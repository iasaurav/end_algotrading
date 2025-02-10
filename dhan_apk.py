import pandas as pd
name="BANKEX"
trading = "55600PE|20|B"
strike = trading.split("|")[0]
# Read data from URL
url = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"
data = pd.read_csv(url).iloc[:, :15]

# Handle STRIKE_PRICE safely
data['STRIKE_PRICE'] = data['STRIKE_PRICE'].fillna(0).astype(int).astype(str) + data['OPTION_TYPE'].fillna("")
#data['LOT_SIZE'] = data['LOT_SIZE'].fillna(0).astype(int)
data = data.sort_values(by='SM_EXPIRY_DATE')
data['SM_EXPIRY_DATE'] = pd.to_datetime(data['SM_EXPIRY_DATE']).dt.strftime('%d-%m-%Y')

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
#print(data)
data = data[(data['UNDERLYING_SYMBOL'] ==name)&(data['STRIKE_PRICE'] ==strike)]

# Display filtered data
print(data)








exchange_token=int(data.iloc[0, 2])
lot_size=int(data.iloc[0, 11])
tradingsymbol=data.iloc[0, 8]
dhan_segment= data.iloc[0, 0]

print(exchange_token,lot_size,tradingsymbol,dhan_segment)


#strike|quantity|BUYSELL|NAME|SEGMENT





from dhanhq import dhanhq
client_id='1101112645'
access_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzM5NTIwNTY2LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMTExMjY0NSJ9.tgEc6XqJPRTKVjSHlbKYxS9d-Dj9-XeTLxg_LOcbYzYLzq4TBky55tuqBwgZ5IpRGXAm9GJO0ORc34-rEq6w5A'


# Initialize the dhanhq object with the client_id and access_token
dhan = dhanhq(client_id, access_token)


if dhan_segment == "NSE":
    result = dhan.NSE_FNO
elif dhan_segment == "BSE":
    result = dhan.BSE_FNO
elif dhan_segment == "MCX":
    result = dhan.MCX


purchase_quantity=int(trading.split("|")[1])


side = trading.split("|")[2]
if side == 'B':
    bookresult = dhan.BUY
elif side == 'S':
    bookresult = dhan.SELL


new_quantity = int(purchase_quantity) * int(lot_size)
print(f"you traded\n{tradingsymbol}\n purchase_quantity-:{new_quantity}")



# Place order
dhan.place_order(
    tag='',
    transaction_type=bookresult,
    exchange_segment=result,
    product_type=dhan.INTRA,
    order_type=dhan.LIMIT,
    validity='DAY',
    security_id=str(exchange_token),
    quantity=new_quantity,
    disclosed_quantity=0,
    price=80,
    trigger_price=0,
    after_market_order=False,#False
    amo_time='OPEN',
    bo_profit_value=0,
    bo_stop_loss_Value=0,
    #drv_expiry_date=None,
    #drv_options_type=None,
    #drv_strike_price=None
)

#EXCH_ID,SECURITY_ID,DISPLAY_NAME,LOT_SIZE,SM_EXPIRY_DATE,STRIKE_PRICE







import pandas as pd

trading = "IDEA|20|B"
strike = trading.split("|")[0]
# Read data from URL
url = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"
data = pd.read_csv(url).iloc[:, :15]
data = data[(data['UNDERLYING_SYMBOL'] ==trading.split("|")[0])&(data['EXCH_ID'] =="NSE")&(data['INSTRUMENT_TYPE'] =="ES")]
data['ISIN'] = "NSE_EQ|"+data['ISIN']
# Display filtered data
print(data)

exchange_token=int(data.iloc[0, 2])
lot_size=int(data.iloc[0, 11])
tradingsymbol=data.iloc[0, 8]
dhan_segment= data.iloc[0, 0]

print(exchange_token,lot_size,tradingsymbol,dhan_segment)




from dhanhq import dhanhq
client_id='1101112645'
access_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzM5NTIwNTY2LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMTExMjY0NSJ9.tgEc6XqJPRTKVjSHlbKYxS9d-Dj9-XeTLxg_LOcbYzYLzq4TBky55tuqBwgZ5IpRGXAm9GJO0ORc34-rEq6w5A'


# Initialize the dhanhq object with the client_id and access_token
dhan = dhanhq(client_id, access_token)


if dhan_segment == "NSE":
    result = dhan.NSE



purchase_quantity=int(trading.split("|")[1])


side = trading.split("|")[2]
if side == 'B':
    bookresult = dhan.BUY
elif side == 'S':
    bookresult = dhan.SELL


new_quantity = int(purchase_quantity) * int(lot_size)
print(f"you traded\n{tradingsymbol}\n purchase_quantity-:{new_quantity}")



# Place order
dhan.place_order(
    tag='',
    transaction_type=bookresult,
    exchange_segment=result,
    product_type=dhan.INTRA,
    order_type=dhan.LIMIT,
    validity='DAY',
    security_id=str(exchange_token),
    quantity=new_quantity,
    disclosed_quantity=0,
    price=80,
    trigger_price=0,
    after_market_order=False,#False
    amo_time='OPEN',
    bo_profit_value=0,
    bo_stop_loss_Value=0,
    #drv_expiry_date=None,
    #drv_options_type=None,
    #drv_strike_price=None
)

#EXCH_ID,SECURITY_ID,DISPLAY_NAME,LOT_SIZE,
