# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Programa Simples de Tabuada ---{RESET}')

# Entrada de dados
num = int(input(f'{YELLOW}Digite um número inteiro:{RESET} '))

print(f'''\n{'-'*16}
|Tabuada do [{CYAN}{num}{RESET}]|
{'-'*16}''')

# Laço de repetição: Mostra a tabuada do número digitado pelo usuário
for i in range(1, 11):
    print(f' {num} x {i} = {num * i}')
