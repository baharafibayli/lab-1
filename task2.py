data=[
    {"day": "Monday", "temp": 5},
    {"day": "Tuesday", "temp": 12},
    {"day": "Wednesday", "temp": 18},
    {"day": "Thursday", "temp": 25},
    {"day": "Friday", "temp": 31},
    {"day": "Saturday", "temp": 28},
    {"day": "Sunday", "temp": 9},
]
to_fahrenheit=list(map(lambda day: day["temp"]*9/5+32,data))
hot_days=list(filter(lambda day: day["temp"]>25,data))
sorted_days=sorted(data, key=lambda day: day["temp"], reverse=True)
lines=list(map(lambda day: day["day"] + ": " + str(day["temp"]), sorted_days))
print("fahrenheit:", to_fahrenheit)
print("hot_days:", hot_days)
print("from warmest to coldest:\n" + "\n".join(lines))
