# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Looping "Infinito" ---{RESET}')

soma = i = 0

# Laço de repetição: lê vários números até que o usuário digite "999"
while True:
    num = int(input(f'{YELLOW}Digite um número inteiro [999 para finalizar]:{RESET} '))
    if num == 999:
        print(VOLTA,LIMPA)
        break
    soma += num
    i += 1

# Resultados finais
print(f'{CYAN}Quantidade de números digitados:{RESET} {i}\n{CYAN}Soma total:{RESET} {soma}')
