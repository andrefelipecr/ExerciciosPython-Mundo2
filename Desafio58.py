# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[1;35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações
from random import randint

print(f'{MAGENTA}--- Jogo da advinhação ---{RESET}')

# Entrada de dados
user_num = 0
chances = 0
comp_num = randint(1,10)
print(f'{CYAN}O computador pensou em um número de 1 até 10.{RESET}')

# Laço de repetição: Verifica se o usuário acertou o número randomizado
while user_num != comp_num:
    user_num = int(input(f'{YELLOW}Tente adivinhar o número:{RESET} '))
    if user_num < 1 or user_num > 10:
        print(f'{RED}Inválido! Digite apenas números no intervalo [1~10]{RESET}')
        continue
    if user_num != comp_num:
        if comp_num > user_num:
            print(f'{RED}You lost :({RESET} Tente um {CYAN}maior{RESET}.')
            chances += 1
        elif comp_num < user_num:
            print(f'{RED}You lost :({RESET} Tente um {CYAN}menor{RESET}.')
            chances += 1
    else:
        chances += 1
        print(f'''{GREEN}Na mosca! Você acertou na {chances}ª chance.{RESET}
        {CYAN}|Número sorteado: {comp_num}|{RESET}''')
