# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Carrinho de Compras ---{RESET}')

# Entrada de dados
total = mais_de_mil = 0
barato = ''
menor_preço = None

# Estrutura de repetição: looping, programa encerra quando usuário escolher parar
while True:
    print('-'*25)
    produto = input(f'{YELLOW}Nome do produto:{RESET} ')
    preço = float(input(f'{YELLOW}Preço de {produto}:{RESET} R$'))
    total += preço
    print('-'*25)
    
    if preço > 1000:
        mais_de_mil += 1
    
    if menor_preço is None or preço < menor_preço:
        menor_preço = preço
        barato = produto
    
    while True:
        continuar = input(f'Deseja continuar? [s/n]: ').strip().upper()[0]
        print(VOLTA,LIMPA)
        if continuar in 'SN':
            break
    
    if continuar == 'N':
        break

print(f'''{MAGENTA}   - CUPOM FISCAL -{RESET}
Total da compra - {GREEN}R${total:.2f}{RESET}
Ao todo {mais_de_mil} produtos custam mais de R$1000.00
Produto mais barato: {barato} que custa R${menor_preço:.2f}''')
