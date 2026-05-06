weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K or L): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Pounds"
    print(f"Your weight in {unit} is {round(weight, 1)} ")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kilograms"
    print(f"Your weight in {unit} is {round(weight, 1)} ")
else:
    print(f"{unit} is not valid")
