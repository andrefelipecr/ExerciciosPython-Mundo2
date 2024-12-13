# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Simulador de Financiamento de Imóvel ---{RESET}')

# Entrada de dados
salário = float(input(f'{YELLOW}Digite o seu salário atual:{RESET} R$'))
imóvel = float(input(f'{YELLOW}Digite o valor total do imóvel:{RESET} R$'))
anos = int(input(f'{YELLOW}Em quantos anos pretende pagar o valor total do imóvel?{RESET} '))
prestações = imóvel / (anos * 12)

# Estrutura Condicional: Validação do financiamento 
if prestações < salário * 0.3:
    print(f'''
    {GREEN}Financiamento Aprovado!{RESET}
    Total de parcelas: x{anos * 12}
    Valor de cada parcela: R${prestações:.2f}
    ''')
else: 
    print(f'''
    {RED}Financiamento Negado!{RESET}
    {CYAN}Motivo:{RESET} O valor das prestações ({RED}R${prestações:.2f}{RESET}) excede 30% do seu salário.
    ''')

# Mensagem Final
print(f'{CYAN}Obrigado por usar o simulador de financiamento!{RESET}')
