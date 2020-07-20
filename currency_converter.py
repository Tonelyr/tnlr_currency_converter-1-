import requests
import json

print("Welcome to the Currency Converter !")
user_currency = input("Convert from: ")
user_desired_currency = input("Convert to: ")
amount = float(input('Amount of ' + user_currency + " to convert to " + user_desired_currency + ": "))

api_link = "https://api.exchangeratesapi.io/latest?base=" + user_currency

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
    raise ValueError("Invalid Value, please check out our Available Currencies at https://pastebin.com/wV17F5wX")
    raise KeyError("Invalid Value, please check out our Available Currencies at https://pastebin.com/wV17F5wX")
# Pastebin of Available Currencies : https://pastebin.com/wV17F5wX