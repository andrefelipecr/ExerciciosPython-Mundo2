# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2k"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações
from time import sleep

print(f'{MAGENTA}--- Menu Interativo ---{RESET}')

num1 = int(input(f'{YELLOW}Digite o 1º valor:{RESET} '))
num2 = int(input(f'{YELLOW}Digite o 2º valor:{RESET} '))
resp = 0

while resp != 5:
    print(f'''
    {'-'*27}
    |{GREEN}{num1:^11}|{num2:^11}{RESET}  |
    {'-'*27}
    |[1] Soma dos valores     |
    |[2] Produto dos valores  |
    |[3] Qual é o maior valor?|
    |[4] Digitar novos valores|
    |[5] Sair                 |
    {'-'*27}''')
    resp = int(input(f'{YELLOW}Sua escolha:{RESET} '))
    
    if resp == 1:
        soma = num1 + num2
        print(f'\nA soma entre {num1} e {num2} é {CYAN}{soma}{RESET}')
    elif resp == 2:
        prod = num1 * num2
        print(f'\nO produto entre {num1} e {num2} é {CYAN}{prod}{RESET}')
    elif resp == 3:
        if num1 > num2:
            print(f'\nO número {CYAN}{num1} é maior{RESET} que {num2}')
        elif num2 > num1: 
            print(f'\nO número {CYAN}{num2} é maior{RESET} que {num1}')
        else:
            print(f'\n{CYAN}Os valores são iguais.{RESET}')
    elif resp == 4:
        num1 = int(input(f'{YELLOW}\nDigite o 1º valor:{RESET} '))
        num2 = int(input(f'{YELLOW}Digite o 2º valor:{RESET} '))
    elif resp == 5:
        print(f'{RED}Saindo do programa...{RESET}')
        sleep(1.5)
    else: 
        print(f'{RED}Opção inválida! Por favor, atente-se ao menu.{RESET}')
