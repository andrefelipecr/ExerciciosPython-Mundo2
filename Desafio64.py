# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Tratamento de Valores ---{RESET}')

num = i = soma = 0
num = int(input(f'{YELLOW}Digite um número inteiro [999 para finalizar]:{RESET} '))

while num != 999:
    soma += num
    i += 1
    num = int(input(f'{YELLOW}Digite um número inteiro [999 para finalizar]:{RESET} '))

print(VOLTA,LIMPA)
print(f'-'*34)
print(f'{CYAN}Quantidade de números digitados:{RESET} {i}\n{CYAN}Soma dos valores:{RESET} {soma}')
