data=[
    {"day": "Monday", "temp": 5},
    {"day": "Tuesday", "temp": 12},
    {"day": "Wednesday", "temp": 18},
    {"day": "Thursday", "temp": 25},
    {"day": "Friday", "temp": 31},
    {"day": "Saturday", "temp": 28},
    {"day": "Sunday", "temp": 9},
]
temps={}
for day in data:
  temps[day["day"]]=day["temp"]
def update_values(old_dict,callback):
  result={}
  for key in old_dict:
    old_value=old_dict[key]
    new_value=callback(old_value)
    result[key]=new_value
  return result
def to_category(temp):
  if temp<10:
    return "Cold"
  elif temp<=25:
    return "Normal"
  else:
    return "Hot"
fahrenheit=update_values(temps,lambda c: c*9/5 +32 )
print("farenheit:",fahrenheit)
categories=update_values(temps, to_category)
print("original_data:", temps)
print("categories:",categories)
