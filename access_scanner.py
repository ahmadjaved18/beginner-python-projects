badge = [2, 4, 6, 7, 8, 9, 12, 13, 14]
approved = []
denied = []
while True:
    name = input("Enter your name (or done to finish): ")

    if name.lower() == "done":
        break

    try:
        badge_num = int(input(f"{name} What is your badge number: "))
    except ValueError:
        print('Invalid badge number — must be a whole number.')
        denied.append(name)
        continue

    if badge_num in badge:
        print("Access approved ✅")
        approved.append(name)
    else:
        print("Access denied ❌")
        denied.append(name)


print("\n======Access Summary=======")
print("\n✅Approved visitors ")
for people in approved:
    print("-", people.capitalize())
print("⛔Denied visitors ")
for people in denied:
    print("-", people.capitalize())

print("Total access granted = ", len(approved))
print("Total people denied = ", len(denied))