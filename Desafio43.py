# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Índice de Massa Corpórea ---{RESET}')

# Entrada de dados
peso = float(input(f'{YELLOW}Informe seu peso em kg:{RESET} '))
altura = float(input(f'{YELLOW}Informe a sua altura em metros:{RESET} '))
IMC = peso/(altura ** 2)

print(f'{MAGENTA}-{RESET}'*32)

# Estrutura condicional
if IMC < 18.5:
    print(f'''Seu IMC: {IMC:.1f}
Status: {RED}Abaixo do peso{RESET}''')
elif 18.5 <= IMC < 25:
    print(f'''Seu IMC: {IMC:.1f}
Status: {GREEN}Peso normal{RESET}''')
elif 25 <= IMC < 30:
    print(f'''Seu IMC: {IMC:.1f}
Status: {YELLOW}Sobrepeso{RESET}''')
elif 30 <= IMC < 35:
    print(f'''Seu IMC: {IMC:.1f}
Status: {RED}Obesidade grau 1{RESET}''')
elif 35 <= IMC < 40:
    print(f'''Seu IMC: {IMC:.1f}
Status: {RED}Obesidade grau 2{RESET}''')
elif IMC >= 40:
    print(f'''Seu IMC: {IMC:.1f}
Status: {RED}Obesidade grau 3{RESET}''')
    
# Mensagem final
print(f'''
{CYAN}Obrigado por usar nosso simulador de IMC.''')
