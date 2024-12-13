# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações
from datetime import date

print(f'{MAGENTA}--- Informações sobre Alistamento Militar ---{RESET}')

# Entrada de dados
user_year = int(input(f'{YELLOW}Digite o ano em que você nasceu:{RESET} '))
sexo = input(f'{YELLOW}Qual o seu sexo? [M/F]:{RESET} ').upper().strip()

print()

# Cálculo da idade do usuário
idade = date.today().year - user_year

print(f'{CYAN}Sua idade:{RESET} {idade}')

# Estrutura condicional
if sexo == 'M':
    if idade < 18:
        print(f'Faltam apenas {18 - idade} anos. Você ainda vai alistar-se ao serviço militar.')
    elif idade == 18:
        print(f'Este é o ano em que você deve alistar-se ao serviço militar!')
    else:
        print(f'''Você, provavelmente, alistou-se há {idade - 18} anos. 
    {CYAN}Obs.:{RESET} Se não alistou ainda, procure a Junta de Serviço Militar mais próxima.''')
else:
    print(f'O Alistamento Militar não é obrigatório para você.')
