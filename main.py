import json

from automato import Automato

automato_teste = Automato('automato.json')

print("="*51)
print("="*20, "Pytomatos", "="*20)
print("="*51)

criterio_aceite = False
current_state = automato_teste.initial_state

palavra_teste = str(input("Informe a palavra teste para o autômato: "))
print(f'inicia em: {current_state}')
for index, letter in enumerate(palavra_teste):
    current_state = (automato_teste.transitions.get(current_state).get(palavra_teste[index]))
    print(f'recebe: {letter}')
    print(f'vai para: {current_state}')
"""
while True:
    for x in split_palavra:
        for y in automato_teste.transitions:
            for z in automato_teste.transitions[automato_teste.current_state]:
                if split_palavra[x] == automato_teste.transitions[automato_teste.current_state][z][1]:
                    automato_test.current_state = 
                    
                

    if automato_teste.current_state == automato_teste.final_state:
        criterio_aceite = True
        break

if criterio_aceite == True:
    print(f"A palavra {palavra_teste} foi aceita")
else:
    print(f"A palavra {palavra_teste} foi rejeitada")
"""

# if __name__ == '__main__':
    # print(automato_teste)

