# Códigos ANSI para cores
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações
from emoji import emojize
from time import sleep
from datetime import datetime

print(f'{MAGENTA}--- Contagem Regressiva ---{RESET}')

new_year = datetime.today().year + 1

# Laço de repetição: Contagem regressiva de 10 até 1
for i in range(10, 0, -1):
    print(f'{i}!')
    sleep(1.0)
print(emojize(f'FELIZ ANO NOVO!:fireworks::clinking_glasses: Que seu {new_year} seja incrível:sparkles:'))
