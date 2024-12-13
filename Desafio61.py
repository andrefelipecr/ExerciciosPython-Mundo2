# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- P.A. Usando Laço de repetição(while) ---{RESET}')

# Entrada de dados
a1 = int(input(f'{YELLOW}Digite o 1º termo:{RESET} '))
r = int(input(f'{YELLOW}Digite a razão:{RESET} '))
n = int(input(f'{YELLOW}Digite a quantidade de termos iniciais:{RESET} '))
i = 1

print(f'{MAGENTA}-{RESET}'*45)

# Laço de repetição: mostra a progressão aritmética
print('{', end='')
while i <= n:
    print(f'{a1}, ', end='')
    a1 += r
    i += 1
print('...}')
