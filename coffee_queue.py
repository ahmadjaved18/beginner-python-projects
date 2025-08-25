total_price = 0
total_drink = 0

menu = {
    'latte': 3.50,
    'americano': 3.00,
    'espresso': 2.50,
}

while True:
    name = input("Please Enter your name (or done if you want to finish): ")
    if name.lower() == 'done':
        break

    order = input(f"Please {name} enter your order name: ")
    order_key = order.lower().strip()
    if order_key in menu:
        total_price += menu[order_key]
        total_drink += 1
    else:
        print("Your order is not on the menu")
        continue


print("\nYour order summary")
print(f'Total drinks you ordered = {total_drink}')
print(f'Total price = ${total_price:.2f} ')

print("Thank you for visiting")