import requests
import json

print("Welcome to the Currency Converter !")
user_currency = input("Convert from: ") # Starting Currency
user_desired_currency = input("Convert to: ") # Arrival Currency
amount = float(input('Amount of ' + user_currency + " to convert to " + user_desired_currency + ": ")) # Amount to convert

api_link = "https://api.exchangeratesapi.io/latest?base=" + user_currency # API

if type(amount) == float and type(user_currency) and type(user_desired_currency) == str:
    response = requests.get(api_link)
    data = response.text
    parsed = json.loads(data)
    rates = parsed["rates"]

    for currency, rate in rates.items():
        if currency == user_desired_currency:
            conversion = rate * amount
            print("1", user_currency, "=", currency, rate)
            print(amount, user_currency, "=", currency, conversion)
else:
    raise ValueError("Invalid Value, please check out our Available Currencies at https://pastebin.com/wV17F5wX") # Custom Errors
    raise KeyError("Invalid Value, please check out our Available Currencies at https://pastebin.com/wV17F5wX") # Custom Errors
# Pastebin of Available Currencies : https://pastebin.com/wV17F5wX
