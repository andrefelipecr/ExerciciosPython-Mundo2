# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[4;31m"
MAGENTA = "\033[35m"
GREEN = "\033[4;32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações
from datetime import date

print(f'{MAGENTA}--- Sistema de Entrada no Cinema--- {RESET}')
print(f'''Filme: {CYAN}Deadpool & Wolverine{RESET}
Classificação: {RED}+18{RESET}   
''')

# Entrada de dados 1
quant = int(input(f'{YELLOW}Quantas pessoas assistirão ao filme? {RESET}'))
year = date.today().year
maiores = []
menores = []
print()

# Entrada de dados 2
for i in range(1, quant + 1):
    name = input(f'{YELLOW}Nome da {i}ª pessoa:{RESET} ').strip()
    user_year = int(input(f'{YELLOW}Ano de nascimento da {i}ª pessoa:{RESET} '))
    years_old = year - user_year
    print(f'{name}, {years_old} anos')
    print(f'{CYAN}-{RESET}'*40)

    # Preenche a lista dos maiores e menores de idade
    if years_old >= 18:
        maiores.append(name)
    else:
        menores.append(name)

# Mostra quem poderá assistir ao filme
if maiores:
    print(f'{GREEN}Autorizados a assistir ao filme:{RESET}')
    for name in maiores:
        print(f'- {name}')

# Mostra que não poderá assistir ao filme
if menores:
    print(f'{RED}Negados a assistir ao filme:{RESET}')
    for name in menores:
        print(f'- {name}')
