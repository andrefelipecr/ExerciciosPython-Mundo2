# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
print(f'{MAGENTA}--- Análise Básica de Dois Valores ---{RESET}')

# Entrada de dados
n1 = int(input(f'{YELLOW}Digite o 1º valor:{RESET} '))
n2 = int(input(f'{YELLOW}Digite o 2º valor:{RESET} '))

print('='*23)

# Estrutura condicional
if n1 > n2:
    print(f'O {CYAN}primeiro{RESET} valor é maior')
elif n2 > n1:
    print(f'O {CYAN}segundo{RESET} valor é maior')
else:
    print(f'Não existe valor maior, pois os dois são {CYAN}iguais')
