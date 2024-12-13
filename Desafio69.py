# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Análise de Dados ---{RESET}')

# Entrada de dados
mais18 = 0
homens = 0
mulher_menos20 = 0
i = 1

# Estrutura de repetição: looping, usuário escolhe se quer ou não continuar o programa
while True:
    idade = int(input(f'{YELLOW}Informe a idade da {i}ª pessoa:{RESET} '))
    while True:
        sexo = input(f'{YELLOW}Informe o gênero da {i}ª pessoa [m/f]:{RESET} ').strip().upper()[0]
        if sexo in 'MF':
            break
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menos20 += 1
    print('-'*40)
    i += 1
    while True:
        escolha = input(f'Quer continuar? [s/n]: ').strip().upper()[0]
        print(VOLTA,LIMPA)
        if escolha in 'SN':
            break
    if escolha == 'N':
        break

print(f'''{CYAN}Resultados Finais:{RESET}\n{'-'*18}
a) Maiores de 18 anos: {mais18} pessoas
b) Quantos são homens: {homens} pessoas
c) Mulheres com menos de 20 anos: {mulher_menos20} pessoas''')
