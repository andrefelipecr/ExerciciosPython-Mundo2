# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[4;31m"
MAGENTA = "\033[35m"
GREEN = "\033[4;32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Simulador de Triângulos ---{RESET}')

r = float(input(f'{YELLOW}Comprimento do 1º segmento:{RESET} '))
s = float(input(f'{YELLOW}Comprimento do 2º segmento:{RESET} '))
t = float(input(f'{YELLOW}Comprimento do 3º segmento:{RESET} '))

print(f'{MAGENTA}-{RESET}'*31)

# Estrutura condicional
if r < s + t and s < r + t and t < r + s:
    print(f'Os valores de segmentos {r, s, t} {GREEN}podem formar um triângulo{RESET} ', end='')
    if r != s != t != r:
        print(f'{CYAN}ESCALENO!{RESET}')
    elif (r == s and s != t) or (r == t and t != s) or (t == s and s != r):
        print(f'{CYAN}ISÓSCELES!{RESET}')
    elif r == s == t:
        print(f'{CYAN}EQUILÁTERO!{RESET}')
else: 
    print(f'Os valores de segmentos {r, s, t} {RED}não podem formar um triângulo{RESET}.')
