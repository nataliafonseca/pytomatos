import json
from automato import Automato

automato_teste = Automato('automato.json')

print("="*51)
print("="*20, "Pytomatos", "="*20)
print("="*51)

criterio_palavra = False
criterio_aceite = False
current_state = automato_teste.initial_state

palavra_teste = str(input("Informe a palavra teste para o autômato: "))

for x in range(0, len(palavra_teste)):
    if palavra_teste[x] in automato_teste.alphabet:
        criterio_palavra = True
    else:
        criterio_palavra = False
        break

if criterio_palavra == False:
    print(f"A palavra {palavra_teste} não está no alfabeto do autômato")
else:
    print(f'inicia em: {current_state}')

    for index, letter in enumerate(palavra_teste):
        current_state = (automato_teste.transitions.get(current_state).get(palavra_teste[index]))
        print(f'recebe: {letter}')
        print(f'vai para: {current_state}')

    if current_state == automato_teste.final_state:
        criterio_aceite = True
        print(f"A palavra {palavra_teste} foi aceita")
    else:
        print(f"A palavra {palavra_teste} foi rejeitada")

"""

if __name__ == '__main__':
    print(automato_teste)

"""