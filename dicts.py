forecast = {
    "city": "Москва",
     "temperature": int("20")
     }
print(forecast["city"])
forecast["temperature"] = forecast["temperature"] - 5
print(forecast)

print(forecast.get("country", "Россия"))

forecast["data"] = "27.05.2019"
print(len(forecast))