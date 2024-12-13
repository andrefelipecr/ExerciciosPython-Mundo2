# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

#importações
from datetime import date

print(f'{MAGENTA}--- Nível de Experiência do Desenvolvedor ---{RESET}')

# Entrada de dados
user_year = int(input(f'{YELLOW}Em que ano você começou sua carreira de programador?{RESET} '))
exp_user = date.today().year - user_year

print()
print(f'{CYAN}Anos de expêriencia:{RESET} {exp_user}')

if exp_user <= 2:
    print(f'{GREEN}JUNIOR:{RESET} está focado em aprender e desenvolver novas skills.')
elif exp_user <= 5:
    print(f'{GREEN}PLENO:{RESET} já possui uma boa base técnica.')
elif exp_user <= 10:
    print(f'{GREEN}SÊNIOR:{RESET} experiência consolidada!')
elif exp_user <=15:
    print(f'{GREEN}ESPECIALISTA:{RESET} expert em áreas específicas de tecnologia.')
else:
    print(f'{GREEN}LÍDER:{RESET} faz a gestão de equipe, produtos ou departamentos técnicos.')
