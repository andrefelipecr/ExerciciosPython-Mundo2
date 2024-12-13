# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Somatória de Sequências Numéricas --- {RESET}')

num = int(input(f'{YELLOW}Digite o último valor da sequência:{RESET} '))
soma = 0

# Mostra o menu de opções para o usuário
print(f'''{'-'*40}
[{CYAN}1{RESET}] Somar valores {CYAN}pares{RESET} entre 1 e {num}
[{CYAN}2{RESET}] Somar valores {CYAN}ímpares{RESET} entre 1 e {num}
[{CYAN}3{RESET}] Somar {CYAN}todos{RESET} os valores entre 1 e {num}
{'-'*40}''')
resp = int(input(f'{YELLOW}Sua escolha:{RESET} '))
print('-'*40)

# Estrutura condicional: Se o usuário digitou 1; 2 ou 3
if resp == 1:
    # Laço de repetição: Soma todos os valores pares da sequência
    for i in range(1, num+1):
        if i % 2 == 0:
            soma += i
            if i < num - 1:
                print(f'{i} + ', end='')
            else:
                print(f'{i} = ', end='')
elif resp == 2:
    # Laço de repetição: Soma todos os valores ímpares da sequência
    for i in range(1, num+1):
        if i % 2 == 1:
            soma += i
            if i < num - 1:
                print(f'{i} + ', end='')
            else:
                print(f'{i} = ', end='')
elif resp == 3:
    # Laço de repetição: Soma todos os valores da sequência
    for i in range(1, num+1):
            soma += i
            if i < num:
                print(f'{i} + ', end='')
            else:
                print(f'{i} = ', end='')
    
print(f'{GREEN}{soma}{RESET}')
