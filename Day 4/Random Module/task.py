import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_number = random.random() * 10
# print(random_number)
#
# random_number2 = random.uniform(1, 10)
# print(random_number2)

print("Heads or Tails????")

value_coin = random.randint(0, 1)

if value_coin == 0:
    print("Heads")
else:
    print("Tails")
