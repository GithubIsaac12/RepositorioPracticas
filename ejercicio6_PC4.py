
#ejercicio 6
'''Para este problema deberá generar una base de datos llamada “cryptos” donde generará una tabla
llamada bitcoin en el cual deberá colocar el precio del bitcoin según la moneda USD, GBP, EUR. Deberá
tomar como base lo realizado en el problema 1.'''


import requests
import sqlite3
from datetime import datetime
conn = sqlite3.connect('cryptos.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin(
currency TEXT PRIMARY KEY, price REAL, date TEXT)''')

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
bitcoin_prices = {}

for currency in data['bpi']:
    price = data['bpi'][currency]['rate']
    bitcoin_prices[currency] = price
    
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for currency, price in bitcoin_prices.items():
    cursor.execute('''
        INSERT OR REPLACE INTO bitcoin (currency, price, date)
        VALUES (?, ?, ?)
    ''', (currency, price, date))
    
conn.commit()
conn.close()
