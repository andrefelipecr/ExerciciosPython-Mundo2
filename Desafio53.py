# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- É um Palíndromo? ---{RESET}')

# Entrada de dados
msg = input(f'{YELLOW}Digite uma frase:{RESET} ').strip().upper()
string = msg.replace(' ', '')

# Mostra a frase no sentido normal
print(f'\n{CYAN}Frase normal:{RESET} {msg}')

# Mostra a frase no sentido contrário
print(f'{CYAN}Frase ao contrário:{RESET} ', end='')
for i in range(len(string)):
    print(string[-1::-1][i], end='')

print()

# Estrutura condicional: Verifica se a frase é um palíndromo
if string == string[-1::-1]:
    print(f'\nEsta frase {GREEN}é um palíndromo!{RESET}')
else:
    print(f'\nEsta frase {RED}não é um palíndromo{RESET}.')
