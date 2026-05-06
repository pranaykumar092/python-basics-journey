operator = input ("Enter an operator (- + / *): ")
num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value"))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2    
else:
    print ("Wrong input")