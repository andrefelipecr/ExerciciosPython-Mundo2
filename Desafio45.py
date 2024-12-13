# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações
from random import randint
from time import sleep

print(f'{MAGENTA}--- Pedra, Papel, Tesooooura! ---{RESET}')

# Menu do jogo
print('-'*13)
print(f'|({CYAN}1{RESET}) Pedra  |')
print(f'|({CYAN}2{RESET}) Papel  |')
print(f'|({CYAN}3{RESET}) Tesoura|')
print('-'*13)

# Entrada de dados
user = int(input(f'{YELLOW}Sua escolha:{RESET} '))
comp = randint(1,3)
print('='*15)

print('Aguardando resposta do adversário...')
sleep(1.5)
print()

# Estrutura condicional
if user >= 1 and user <= 3:
    if user == 1 and comp == 2:
        print('|PEDRA X PAPEL|')
        print(f'{RED}Perdeu! Você foi embrulhado pelo oponente.{RESET}')
    elif user == 1 and comp == 3:
        print('|PEDRA X TESOURA|')
        print(f'{GREEN}Ganhou! Você quebrou o oponente no meio.{RESET}')
    elif user == 2 and comp == 1:
        print('|PAPEL X PEDRA|')
        print(f'{GREEN}Ganhou! Você embrulhou seu oponente.{RESET}')
    elif user == 2 and comp == 3:
        print('|PAPEL X TESOURA|')
        print(f'{RED}Perdeu! Você foi cortado em pedaços.{RESET}')
    elif user == 3 and comp == 2:
        print('|TESOURA X PAPEL|')
        print(f'{GREEN}Ganhou! Você cortou o oponente em pedaços.{RESET}')
    elif user == 3 and comp == 1:
        print('|TESOURA X PEDRA|')
        print(f'{RED}Perdeu! Você foi quebrado pelo oponente.{RESET}')
    else:
        print(f'{YELLOW}Empate! Jogue outra vez.{RESET}')
else:
    print(f'{RED}Erro:{RESET} por favor, escolha uma das opções acima.')
