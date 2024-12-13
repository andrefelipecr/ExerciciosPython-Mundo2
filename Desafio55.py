# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Análise de Pesos ---{RESET}')

# Laço de repetição: O programa lê 5 pesos e faz uma lista
pesos = [float(input(f'{YELLOW}Digite o {i}º peso:{RESET} ')) for i in range(1,6)]

# Método sort(reverse=True): Ordena os valores do maior para o menor
pesos.sort(reverse=True)

print('-'*34)

print(f'''
{CYAN}Maior peso -> {pesos[0]} kg{RESET}
{pesos[1]:>19} kg
{pesos[2]:>19} kg
{pesos[3]:>19} kg
{CYAN}Menor peso ->  {pesos[4]} kg{RESET}
''')
