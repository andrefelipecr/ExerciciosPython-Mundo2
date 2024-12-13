# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

from random import randint

print(f'{MAGENTA}--- Jogo Par ou Ímpar ---{RESET}')

ganhos = 0

# Laço de repetição: Looping "infinito", programa encerra quando usuário perder o jogo
while True:
    usuario_escolha = input(f'Escolha [P]ar ou [I]mpar: ').upper().strip()[0]
    if usuario_escolha not in "PI":
        print(f'{RED}Erro:{RESET} escolha válida é "p" ou "i". Tente novamente')
        continue
    comp_num = randint(0,10)
    usuario_num = int(input(f'Jogue um valor: '))
    print(VOLTA, LIMPA, VOLTA, LIMPA)
    print(f'\nVocê -> {usuario_num} | {comp_num} <- Computador')
    if (usuario_num + comp_num) % 2 == 0 and usuario_escolha in 'P' or (usuario_num + comp_num) % 2 == 1 and usuario_escolha in 'I':
        print(f'Deu par!') if (usuario_num + comp_num) % 2 == 0 else print('Deu ímpar!')
        print(f'{GREEN}Você venceu!{RESET} Jogue novamente.')
        ganhos += 1
        print('-'*30)
    else: 
        print(f'Deu par!') if (usuario_num + comp_num) % 2 == 0 else print('Deu ímpar!')
        print(f'{RED}Você perdeu!{RESET} Fim de jogo.')
        break

print(f'{CYAN}Você venceu {ganhos} vezes. Volte sempre!{RESET}')
