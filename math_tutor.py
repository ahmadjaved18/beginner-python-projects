from random import randrange as r
from time import time as t
import random

quest_no = int(input("How many questions you want:  "))
num_limit = int(input("Tell how high the number should be:  "))

ops_input = input("Which operations? (choose any of + - * / , e.g. +-* ; press Enter for all): ").strip()
if ops_input == "" or ops_input.lower() == "all":
    operations = ['+', '-', '*', '/']
else:
    # keep only valid symbols and preserve order
    operations = []
    for ch in ops_input:
        if ch in ['+', '-', '*', '/'] and ch not in operations:
            operations.append(ch)
    if not operations:
        print("No valid operations chosen — defaulting to all.")
        operations = ['+', '-', '*', '/']

score = 0
# using time module for time
start = t()
# add ans_list for more clarity
ans_list = []

for q in range(quest_no):
    op = random.choice(operations)

    # generate numbers depending on operation
    if op == '+':
        num1, num2 = r(1, num_limit), r(1, num_limit)
        correct = num1 + num2
        prompt = f"{num1} + {num2} = "
    elif op == '-':
        a, b = r(1, num_limit), r(1, num_limit)
        # making subtraction non-negative to keep it simple 
        num1, num2 = max(a, b), min(a, b)
        correct = num1 - num2
        prompt = f"{num1} - {num2} = "
    elif op == '*':
        num1, num2 = r(1, num_limit), r(1, num_limit)
        correct = num1 * num2
        prompt = f"{num1} * {num2} = "
    else:  # op == '/'
        # ensure an integer division: choose divisor and multiply to make dividend
        divisor = r(1, num_limit)
        multiplier = r(1, num_limit)
        dividend = divisor * multiplier
        num1, num2 = dividend, divisor
        correct = dividend // divisor  
        prompt = f"{num1} / {num2} = "

    try:
        user_ans = int(input(prompt))
    except ValueError:
        user_ans = None  #treat invalid input as wrong 

    ans_list.append(f"{prompt.strip()} {correct} : You = {user_ans}")
    if user_ans == correct:
        score += 1

end = t()
print(f"Thank you for playing!\nYour score is {score} out of {quest_no} ({round((score/quest_no * 100))}% result) in {round(end-start,1)} seconds with {round((end-start)/quest_no,1)} second/question")

print("\n===Result summary===\n")
for a in ans_list:
    print(a)
