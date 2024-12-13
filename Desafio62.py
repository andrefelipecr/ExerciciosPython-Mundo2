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
total_termos = n

print(f'{MAGENTA}-{RESET}'*45)

# Laço de repetição: mostra a progressão aritmética
while n != 0:
    print('{', end='')
    for i in range(total_termos):
        print(f'{a1 + i * r}, ', end='')
    print('...}')
    n = int(input(f'\n{YELLOW}Quantos termos você quer mostrar a mais? (Digite 0 para encerrar):{RESET} '))
    total_termos += n
print(VOLTA,LIMPA)
print(f'{CYAN}{total_termos} termos mostrados na P.A.{RESET}')
