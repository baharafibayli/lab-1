data=[
  {"day": "monday", "temp": 5},
  {"day": "tuesday", "temp": 12},
  {"day": "wednesday", "temp": 18},
  {"day": "thursday", "temp": 27},
  {"day": "friday", "temp": 30},
  {"day": "saturday", "temp": 9 },
  {"day": "sunday", "temp": 22},
]
to_fahrenheit=list(map(lambda day: day["temp"]*9/5+32,data))
hot_days=list(filter(lambda day: day["temp"]>25,data))
sorted_days=sorted(data, key=lambda day: day["temp"], reverse=True)
lines=list(map(lambda day: day["day"] + ": " + str(day["temp"]), sorted_days))
print("fahrenheit:", to_fahrenheit)
print("hot_days:", hot_days)
print("from warmest to coldest:\n" + "\n".join(lines))
