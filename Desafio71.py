# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Simulador de Caixa Eletrônico ---{RESET}')

# Entrada de dados: lê o valor do saque
saque = int(input(f'{YELLOW}Insira a quantia desejada:{RESET} {GREEN}R$'))

print(f'''{RESET}{'='*22}
|{CYAN}Sacando dinheiro ...{RESET}|
{'='*22}''')

# Laço de repetição: Contador de cédulas(50, 20, 10 e 1)
while True:
        if saque >= 50:
            nota_50 = saque // 50
            saque %= 50
            print(f'|{nota_50:>3} nota(s) de R$50 |')
        elif saque >= 20:
            nota_20 = saque // 20
            saque %= 20
            print(f'| {nota_20:>2} nota(s) de R$20 |')
        elif saque >= 10:
            nota_10 = saque // 10
            saque %= 10
            print(f'| {nota_10:>2} nota(s) de R$10 |')
        else:
            moeda_1 = saque
            print(f'| {moeda_1:>2} moeda(s) de R$1 |')
            break
        if saque == 0:
            break
print('-'*22)
print(f'{CYAN}Obrigado por usar nosso simulador. Volte sempre!{RESET}')
