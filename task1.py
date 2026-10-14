data=[
  {"day": "monday", "temp": 5},
  {"day": "tuesday", "temp": 12},
  {"day": "wednesday", "temp": 18},
  {"day": "thursday", "temp": 27},
  {"day": "friday", "temp": 30},
  {"day": "saturday", "temp": 9 },
  {"day": "sunday", "temp": 22},
]
counts={"cold": 0, "normal": 0, "hot": 0}
total=0
for day in data:
  temp=day["temp"]
  total+=temp
  if temp<10:
    counts["cold"]+=1
  elif temp<=25:
    counts["normal"]+=1
  else:
    counts["hot"]+=1
average=total/len(data)
print(counts)
print(round(average,2))
