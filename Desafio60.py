# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações
from math import factorial
from time import sleep

print(f'{MAGENTA}--- Fatorial de Um Número ---{RESET}')

# Entrada de dados
num = int(input(f'{YELLOW}Digite um número:{RESET} '))
i = num

print(f'\n{CYAN}CALCULANDO...{RESET}')
sleep(1.5)

print(f'{CYAN}{num}!{RESET}', end=' = ')

# Laço de repetição: mostra equação do fatorial do número
while i != 0:
    print(i, end='')
    if i > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    i -= 1

print(f'{GREEN}{factorial(num)}{RESET}')
