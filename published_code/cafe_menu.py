menu = {"pizza": 90.88,
        "burger": 50.33,
        "nachos": 50.00,
        "dal chawal": 60.00,
        "rajma poori": 80.00,
        "biscuit": 10.10,
        "chai": 10.00,
        "namkeen": 70.00}
cart = []
total = 0

print("---------Menu---------")
for key, value in menu.items():
    print(f"{key:15} : {value:.2f}")
print("----------------------")

while True:
    food = input("Enter the food from the menu (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("------Your Order-------")
         
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    
print()
print(f"Your Total is ${total:.2f}")
 