# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Sistema de Boletim do Aluno ---{RESET}')

# Entrada de dados
print('='*22)
n1 = float(input(f'{YELLOW}Digite a 1ª nota:{RESET} '))
n2 = float(input(f'{YELLOW}Digite a 2ª nota:{RESET} '))
print('-'*22)

# Cálculo da média das notas
media = (n1 + n2) / 2

# Estrutura condicional
if media >= 7:
    print(f'''Média do Aluno: {GREEN}{media:.1f}{RESET}
Situação: {GREEN}APROVADO''')
elif media >= 5 and media < 7:
    print(f'''Média do Aluno: {YELLOW}{media:.1f}{RESET}
Situação: {YELLOW}EM RECUPERAÇÃO''')
else:
    print(f'''Média do Aluno: {RED}{media:.1f}{RESET}
Situação: {RED}REPROVADO''')
    
print(f'{RESET}='*22)
