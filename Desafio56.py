# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Análise de Dados Básica ---{RESET}')

# Atribuição de variáveis
soma_idades = 0
velho_idade = 0
c = 0

# Laço de repetição: Programa lê nome, idade e sexo de 4 pessoas
for i in range(1,5):
    nome = input(f'{YELLOW}Digite o nome da {i}ª pessoa:{RESET} ').strip()
    idade = int(input(f'{YELLOW}Digite a idade da {i}ª pessoa:{RESET} '))
    sexo = input(f'{YELLOW}Sexo [M/F]:{RESET} ').strip().upper()
    print(f'{MAGENTA}-{RESET}'*35)
    
    # Calcula a soma das 4 idades
    soma_idades += idade
    
    # Verifica quem é o homem mais velho
    if sexo == 'M' and idade > velho_idade:
        velho_idade = idade
        velho = nome
    # Contagem de mulheres que têm menos de 20 anos
    if sexo == 'F' and idade < 20:
        c += 1

print(f'''
{CYAN}Média das idades:{RESET} {(soma_idades / 4):.1f} anos
{CYAN}Nome e idade do homem mais velho:{RESET} {velho}, {velho_idade}
{CYAN}Quantidade de mulheres com menos de 20 anos:{RESET} {c}
''')
