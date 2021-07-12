# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 02:53:00 2021

@author: usetr2
"""
import requests
from datetime import datetime
class CurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']
        self.date=self.data["date"]
        self.time=self.data["time_last_updated"]
    def dates(self):
        return self.date
    def times(self):
        ts = int(self.time)
        timings=(datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        return timings
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount
    
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    x=input("enter intial currency code in CAPS ")
    y=input("enter final currency code in CAPS ")
    amt=int(input("enter the amount to be converted "))
    t=converter.times().strip(" ")
    print("The data was last updated on", t)
    print(converter.convert(x,y,amt))
    