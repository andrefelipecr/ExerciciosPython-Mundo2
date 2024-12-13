# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Somatória de quaisquer valores ---{RESET}')

# Mostra o menu de opções para o usuário
print(f'''{'-'*28}
[{CYAN}1{RESET}] Somar apenas os pares  |
[{CYAN}2{RESET}] Somar apenas os ímpares|
[{CYAN}3{RESET}] Somar todos os valores |
{'-'*28}''')

resp = int(input(f'{YELLOW}Sua escolha:{RESET} '))
print('-'*28)
soma = 0

# Estrutura condicional: Se o usuário digitou 1; 2 ou 3
if resp == 1:
    # Laço de repetição: Verifica e soma os valores pares
    for i in range(1, 7):
        num = int(input(f'{YELLOW}Digite o {i}º valor:{RESET} '))
        if num % 2 == 0:
            soma += num
    print(f'A soma dos números {CYAN}pares{RESET} digitados é {GREEN}{soma}{RESET}.')
elif resp == 2:
    # Laço de repetição: Verifica e soma os valores ímpares
    for i in range(1, 7):
        num = int(input(f'{YELLOW}Digite o {i}º valor:{RESET} '))
        if num % 2 == 1:
            soma += num
    print(f'A soma dos números {CYAN}ímpares{RESET} digitados é {GREEN}{soma}{RESET}.')
else:
    #Laço de repetição: Soma todos os 6 valores digitados
    for i in range(1, 7):
        num = int(input(f'{YELLOW}Digite o {i}º valor:{RESET} '))
        soma += num
    print(f'A soma dos números digitados é {GREEN}{soma}{RESET}.')
        