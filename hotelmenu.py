menu = {
  'pizza':90,
  'pasta':80,
  'burger':60,
  'salad':40,
  'coffee':50,
  'Pizza':90,
  'Pasta':80,
  'Burger':60,
  'Salad':40,
  'Coffee':50,
}

print("\n ****Welcome to Python Restaurant****")
print("Pizza: Rs90\nPasta: Rs80\nBurger: Rs60\nSalad: Rs40\nCoffee: Rs50")

order_total = 0

item_1 = input("Enter name of item you want to order = ")
if item_1 in menu:
  order_total += menu[item_1]
  print(f"Your item {item_1} has been added to your order")

else:
  print(f"Ordered item {item_1} is not available yet")

another_item = input("Do you want to add another item? (yes/no)")   
if another_item == "yes":
  item_2 = input("Enter the name of second item =")
  if item_2 in menu:
    order_total += menu[item_2]
    print(f"Item {item_2} has been added to your order")
  else:
    print(f"Ordered item {item_2} is not available!..")

print(f"The total amount of items to pay is {order_total}")
