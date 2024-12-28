weight = 12.3
# Ground Shipping
if weight <= 2.0:
  price = (weight * 1.5) + 20
elif weight <= 6.0:
  price = (weight * 3) + 20
elif weight <= 10.0:
  price = (weight * 4) + 20
else:
  price = (weight * 4.75) + 20
# Ground Shipping Premium
price2 = 125.0
# Drone Shipping
if weight <= 2.0:
  price3 = weight * 4.5
elif weight <= 6.0:
  price3 = weight * 9
elif weight <= 10.0:
  price3 = weight * 12
else:
  price3 = weight * 14.25

# display all shipping prices to the customer
print(price)
print(price2)
print(price3)

# determine which is the cheapest for them, printing out name and price
if price < price2 and price < price3:
  print("The cheapest shipping method is Ground Shipping, at $" + str(price))
elif price2 < price and price2 < price3:
  print("The cheapest shipping method is Ground Shipping Premium, at $" + str(price2))
else: 
  print("The cheapest shipping method is Drone Shipping, at $" + str(price3))
