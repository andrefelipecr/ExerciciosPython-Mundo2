# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Sêquencia de Fibonacci ---{RESET}')

limit = int(input(f'{YELLOW}Quantidade de valores na sequência:{RESET} '))
print(VOLTA,LIMPA)

# Entrada de dados
a = 0
b = 1
c = a + b
i = 0

print(f'''{'-'*35}
Sequência de {CYAN}Fibonacci({limit} valores){RESET}:
{'-'*35}''')

# Laço de repetição: Mostra Fibonacci
while i < limit:
    print(a, end='')
    print(' ⇨ ', end='') if i < limit - 1 else print('', end='')
    a = b
    b = c
    c = a + b
    i += 1
