"""Simple loyalty points engine.

Points = whole dollars spent * 3
Tier: Bronze < 100 pts, Silver >=100, Gold >=500
"""

purchases = [12, 15, 50]

def earn_points(price):
    whole_dollar = int(price)
    return whole_dollar * 3

def tier_label(points):
    if points >= 500:
        return "Gold"
    elif points >= 100:
        return "Silver"
    else:
        return "Bronze"

while True:
    shop = input("Enter your purchase amount (or done if you finish): ")
    if shop.lower() == "done":
        break
    try:
        amount = float(shop)
        purchases.append(amount)
    except ValueError:
        print('Please enter a valid amount (numbers only)')

total_spent = 0
total_points = 0

for amount in purchases:
    total_spent += amount
    total_points += earn_points(amount)

label_tier = tier_label(total_points)

print("=====Loyalty points summary======")
print(f"\nTotal amount spent = ${total_spent:.2f}")
print(f"loyalty points earn =  {total_points} points")
print("loyalty label = ", label_tier)