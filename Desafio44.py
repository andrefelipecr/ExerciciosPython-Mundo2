# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Simulador de Compra de um Produto ---{RESET}')

preço = float(input(f'{YELLOW}Valor original do produto:{RESET} R$'))

print()

# Menu de pagamento
print(f'''{CYAN} Meios de pagamento:{RESET}
{'-'*56}
|{CYAN}1){RESET} À vista (Dinheiro/Pix)          -> Desconto de 10% |
|{CYAN}2){RESET} À vista (Cartão)                -> Desconto de  5% |
|{CYAN}3){RESET} Parcelar em até 2x (Cartão)     -> Sem Juros       |
|{CYAN}4){RESET} Parcelar em mais vezes (Cartão) -> 20% de juros    |
{'-'*56}''')

resp = int(input(f'{YELLOW}Sua escolha:{RESET} '))
print('-'*56)

#Estrutura condicional 
if resp >= 1 and resp <= 4:
    print(f'{GREEN}Compra Aprovada!{RESET}')
    if resp == 1:
        print(f'Valor final do produto: R${(preço * 0.9):.2f}')
    elif resp == 2:
        print(f'Valor final do produto: R${(preço * 0.95):.2f}')
    elif resp == 3:
        print(f'Valor final do produto: 2x de R${(preço * 0.5):.2f}')
        parcelas = 2
    elif resp == 4:
        parcelas = int(input(f'{YELLOW}Em quantas parcelas deseja pagar?{RESET} '))
        print('-'*56)
        print(f'Valor final do produto: {parcelas}x de R${(preço * 1.2 / parcelas):.2f}')
else:
    print(f'''{RED}Inválido!{RESET}
{CYAN}Motivo:{RESET} A sua escolha não está em uma das opções acima.''')
    
# Mensagem final
print(f'{CYAN}Obrigado por usar o nosso simulador de compras!{RESET}')
