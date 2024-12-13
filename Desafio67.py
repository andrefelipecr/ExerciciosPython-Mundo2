# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Tabuada 3.0 ---{RESET}')

# Laço de repetição: Looping, programa encerra quando usuário digitar 0
while True:
    num = int(input(f'{YELLOW}Digite um número para ver a tabuada [0 para sair]: {RESET} '))
    print(VOLTA,LIMPA)
    if num == 0:
        break
    print(f'| TABUADA DO [{CYAN}{num}{RESET}] |')
    for i in range(1, 11):
        print(f'{num:>4} x {i} = {num * i}')
    print('-'*36)

print(f'{GREEN}Obrigado por usar nosso programa!{RESET}')
