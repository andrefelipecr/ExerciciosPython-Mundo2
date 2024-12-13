# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- É um Número Primo? ---{RESET}')

# Entrada de dados
num = int(input(f'{YELLOW}Digite um número inteiro:{RESET} '))
divisores = 0

print()

# Laço de repetição: Conta quantos divisores tem o número
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1

# Estrutura condicional: Verifica se o valor digitado é ou não um número primo
if divisores == 2:
    print(f'O número {num} {GREEN}é primo!{RESET}')
else:
    print(f'O número {num} {RED}não é primo{RESET}.')
