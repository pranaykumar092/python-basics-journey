pesos_to_usd = 60
rupees_to_usd = 70 
dhiram_to_usd = 100

pesos = int(input("what do you have left in pesos? "))
rupees = int(input("what do you have left in rupees? "))
dhiram = int(input("what do you have left in dhiram? "))

total = ((pesos/pesos_to_usd) + (rupees/rupees_to_usd) + (dhiram/dhiram_to_usd))

print (total)