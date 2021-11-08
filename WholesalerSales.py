'''
Wyatt Combs
This program is intended to calculate the total cost, number of items, and volume of a wholesaler purchase using lists.
It also calculates the total number of 20' and 40' containers needed to ship
'''
product_codes = ["LT", "ST", "HS", "LC", "PS", "MD"] #List of strings
shipping_volumes = [5, 3.5, 1, 1.5, 2.3, 0.7] #List of numbers (this and line below)
unit_prices = [799, 497, 199, 849, 299, 129]
total_price = 0
total_volume = 0
num_items = 0

print("--Wholesaler Sales Calculator (Version 1.0)--")

valid_quantity = True #Boolean Flag
while valid_quantity == True:
  valid_quantity = False
  
  user_code = input("What is the product code of the item?")
  user_quantity = int(input("What quantity of this product would you like(Type 0 to end program)? "))
  if user_quantity == 0: #Breaks from while loop with invalid quantity
    print("Program ended.")
    break
  
  for i, a_code in enumerate(product_codes):
    if a_code == user_code:
      total_price += (unit_prices[i] * user_quantity)
      total_volume += (shipping_volumes[i] * user_quantity)
      num_items += user_quantity
      valid_quantity = True
      break
  
  print("Items added.") #Print statement only when items are added

from math import ceil, floor #Imported functions
num_ship_40 = floor(total_volume / 2390)
num_ship_20 = ceil((2 / 2390) * (total_volume % 2390)) #Determines 20' containers needed AFTER using 40' containers
if num_ship_20 == 2:
  num_ship_40 += 1
  num_ship_20 -= 2

print("Total Items: " + str(num_items) + ". Total price: $" + str(total_price) + ". Total Shipping Volume: " + str(total_volume) + " cubic feet.")
print("The order will ship in " + str(num_ship_40) + " 40' shipping containers and " + str(num_ship_20) + " 20' shipping containers.")
