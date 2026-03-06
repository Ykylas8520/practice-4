import datetime

# Example 1: 
a = datetime.now()
print(a)

# Example 2: 
b = datetime(2024, 5, 10)
print(b)

# Example 3: 
print(a.strftime("%Y-%m-%d"))
print(a.strftime("%H:%M:%S"))

# Example 4: 
d1 = datetime(2024, 1, 1)
d2 = datetime(2024, 1, 10)
print(d2 - d1)

# Example 5: 
new_date = d1 + timedelta(days=7)
print(new_date)
