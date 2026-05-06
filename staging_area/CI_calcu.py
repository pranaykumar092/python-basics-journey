# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the Principle Amount: "))
#     if principle < 0:
#         print("The principle cant be less than or equal to zero")

# while rate <= 0:
#     rate = float(input("Enter the rate interest: "))
#     if rate < 0:
#         print("The rate cant be less than or equal to zero")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("The time cant be less than or equal to zero")

# total = principle * pow((1 + rate/100), time)
# print(f"The balance after {time} year/s: {total} Rupees")




principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the Principle Amount: "))
    if principle < 0:
        print("The principle cant be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the rate interest: "))
    if rate < 0:
        print("The rate cant be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("The time cant be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate/100), time)
print(f"The balance after {time} year/s: {total} Rupees")