phone_input = input("Enter a phone number(in any format): ")
cleaned = phone_input.strip()

for char in [",", "(", ":", ")", "."]:
    cleaned = cleaned.replace(char, " ")

parts = cleaned.split()
joint_digits = "".join(parts)

if joint_digits.isdigit() and len(joint_digits) == 11:
    area = joint_digits[0:3]
    mid = joint_digits[3:6]
    end = joint_digits[6:]
    print(f'Formatted number = ({area}) {mid}-{end}')
else:
    print(f'Please enter 11 digits number')


#we can also change it to id card number formatter