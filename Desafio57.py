# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

from random import choice

print(f'{MAGENTA}--- Chá Revelação ---{RESET}')

opçoes = ['MENINO', 'MENINA']
sexo = choice(opçoes)
resp = ''

while resp != sexo:
    resp = input(f'{YELLOW}Qual é o seu palpite?{RESET} ').upper().strip()
    if resp not in opçoes:
        print(f'{RED}Invalido! Digite apenas "menino" ou "menina"{RESET}')
        continue
    if resp != sexo:
        print(f'{RED}Tente novamente!{RESET}')
    else:
        cor = CYAN if sexo == 'MENINO' else MAGENTA
        print(f'Parabéns, você acertou! O bebê é {cor}{sexo.lower()}{RESET}')
