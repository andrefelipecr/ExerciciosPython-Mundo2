# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Enésimos Primeiros Termos de uma P.A. ---{RESET}')

# Entrada de dados
a1 = int(input(f'{YELLOW}Digite o 1º termo:{RESET} '))
r = int(input(f'{YELLOW}Digite a razão:{RESET} '))
n = int(input(f'{YELLOW}Digite a posição do último termo:{RESET} '))
an = 0

print(f'{MAGENTA}-{RESET}'*45)

# Mostra a progressão aritmética
print('{', end='')
for n in range (1, n + 1):
    an = a1 + (n - 1)*r
    print(an, end=', ')
print('...}')
