# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Média, Maior e Menor dos Valores ---{RESET}')

list = []
resp = 'S'
soma = quantidade = 0

while resp == 'S':
    num = int(input(f'{YELLOW}Digite um número inteiro:{RESET} '))
    soma += num
    quantidade += 1
    list.append(num)
    resp = input(f'Deseja continuar? [s/n]: ').strip().upper()[0]
    print(VOLTA,LIMPA)

list.sort(reverse=True)
print(f'''{'-'*40}
A {CYAN}Média{RESET} dos valores digitados: {(soma/quantidade):.2f}
{CYAN}Maior{RESET} valor digitado: {list[0]}
{CYAN}Menor{RESET} valor digitado: {list[-1]}''')
