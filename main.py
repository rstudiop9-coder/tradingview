from tv_get_csv import generate_csv

#inputs
symbol_name="MCX:GOLD1!"
username = 'rstudiop9@gmail.com'
password = 'Glady@2001'

# symbol_name="NSE:NIFTY1!"
frequency="1_day" #"1_minute", "1_day" , "1_week", "1_month"

df =generate_csv(username,password,symbol_name,frequency)
