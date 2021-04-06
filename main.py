import json
from automato import Automato
from time import sleep
from lib.interface import menu, cabecalho


cabecalho(f'{"="*20} Pytomatos {"="*20}')

while True:
    automato = Automato('automato.json')

    resposta = menu(['Imprimir detalhes do autômato',
                     'Testar palavra',
                     'Sair do sistema'])

    if resposta == 1:
        print()
        cabecalho('Opção 1 - Imprimir detalhes do autômato')
        print(automato)
        sleep(1)
        print()

    elif resposta == 2:
        print()
        cabecalho('Opção 2 - Testar palavra')
        palavra = input(
            'Informe a palavra que deseja testar: ')
        automato.teste_palavra(palavra)
        sleep(1)
        print()

    elif resposta == 3:
        print()
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break
