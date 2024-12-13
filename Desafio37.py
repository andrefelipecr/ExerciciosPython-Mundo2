# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
from time import sleep

print(f'{MAGENTA}--- Conversor de Número Decimal ---{RESET}')
# Entrada de dados
num = int(input(f'{YELLOW}Digite um número inteiro:{RESET} '))

# Mostra o menu
print(f'''{'='*22}
|{CYAN}[1]{RESET} para binário    |
|{CYAN}[2]{RESET} para octal      |
|{CYAN}[3]{RESET} para hexadecimal|
{'='*22}''')
resp = int(input(f'|{YELLOW}Sua escolha:{RESET} '))
print('='*22)
print(f'''{GREEN}CALCULANDO...{RESET}
''')
sleep(1.5)

# Estrutura condicional
if int(resp) >= 1 and int(resp) <= 3:
    if resp == 1:
        print(f'O número {num} em {CYAN}binário{RESET} é {bin(num)[2:]}')
    elif resp == 2:
        print(f'O número {num} em {CYAN}octal{RESET} é {oct(num)[2:]}')
    elif resp == 3:
        print(f'O número {num} em {CYAN}hexadecimal{RESET} é {hex(num)[2:]}')
else:
    print(f'{RED}Inválido:{RESET} tente novamente.')
