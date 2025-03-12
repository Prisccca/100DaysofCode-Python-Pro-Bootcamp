import random

# Listas de caracteres possíveis
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# Perguntar ao usuário quantos caracteres de cada tipo ele quer
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Criar a senha usando loops for
password_list = []

# Adiciona letras aleatórias
for passletters in range(nr_letters):
    password_list.append(random.choice(letters))

# Adiciona símbolos aleatórios
for passsymbols in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Adiciona números aleatórios
for passnumbers in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Embaralhar a senha para ficar aleatória
random.shuffle(password_list)

# Converter a lista em string
password = "".join(password_list)

print(f"Your password is: {password}")
