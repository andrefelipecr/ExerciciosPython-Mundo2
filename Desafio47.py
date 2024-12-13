# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Valores Pares ou Ímpares ---{RESET}')

num = int(input(f'{YELLOW}Digite o último valor da sequência:{RESET} '))

print(f'''{'-'*25}
[{CYAN}1{RESET}] Pares de 1 até {num}  
[{CYAN}2{RESET}] Ímpares de 1 até {num}
{'-'*25}''')

resp = int(input(f'{YELLOW}Sua escolha:{RESET} '))

print('-'*25)
print('|', end='')

if resp == 1:
    for i in range(1, num+1):
        if i % 2 == 0:
            print(f'{i}|', end='')
elif resp == 2:
    for i in range(1, num+1):
        if i % 2 == 1:
            print(f'{i}|', end='')
else:
    print(f'{RED}Erro:{RESET} por favor, escolha uma das opções acima.')
