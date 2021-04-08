import json
import copy


class Automato:
    def __init__(self, automato_json):
        self.automato_json = automato_json
        self.automato = self.ler_json(automato_json)
        self.tipo = self.automato['type']
        self.alfabeto = self.automato['alphabet']
        self.estado_inicial = self.automato['initial_state']
        self.estados_finais = self.automato['final_states']
        self.transicoes = self.automato['transitions']

    def __repr__(self):
        string = ''
        string += f'Alfabeto: {self.alfabeto}\n'
        string += f'Estado Inicial: {self.estado_inicial}\n'
        string += f'Estado(s) Final(is): {self.estados_finais}\n'
        string += f'Transições: \n'
        for chave, valor in self.transicoes.items():
            string += f'    {chave}: {valor}\n'
        return string

    @staticmethod
    def ler_json(automato_json):
        with open(automato_json) as json_file:
            dicionario = json.load(json_file)
        return dicionario

    def converter_afn_afd(self):
        # Iniciamos a conversão criando um novo dicionário de transições, 
        # copia do original, que receberá as alterações.
        novas_transicoes = copy.deepcopy(self.transicoes)

        # Variável para controle do loop, uma vez que não estejam mais sendo 
        # criados novos estados, podemos parar o loop!
        novo_estado_criado = True

        while novo_estado_criado:
            for estado in self.transicoes:
                for transicao in self.transicoes[estado]:
                    # Para cada transição, os estados destino serão guardados temporariamente em uma lista (transicao_lista)
                    transicao_lista = self.transicoes[estado][transicao]
                    if len(transicao_lista) > 1:
                        # Se, na lista, houver mais de um destino, será criado um novo estado unificando-os
                        novo_estado = ''.join(transicao_lista)
                        novas_transicoes[novo_estado] = {}
                        # O novo estado substituirá os originais no destino da transição
                        novas_transicoes[estado][transicao] = [novo_estado]

                        for letra in self.alfabeto:
                            # Para cada estado presente na lista, checamos os seus respectivos destinos 
                            # para cada letra do alfato, se houverem. Estes destinos serão adicionados, na letra correspondente,
                            # Como transições do novo estado criado.
                            for estado_destino in transicao_lista:
                                if novas_transicoes[estado_destino].get(letra):
                                    if not novas_transicoes[novo_estado].get(letra):
                                        novas_transicoes[novo_estado][letra] = []
                                    already_in = False
                                    for item in novas_transicoes[novo_estado][letra]:
                                        if novas_transicoes[estado_destino][letra][0] in item:
                                            already_in = True
                                    if not already_in:
                                        novas_transicoes[novo_estado][letra] += novas_transicoes[estado_destino][letra]

            # No fim do loop, checamos se foi realizada a criação de algum novo estado, se sim, o controlador permanece True e o loop
            # continuará.
            novo_estado_criado = len(novas_transicoes) > len(self.transicoes)
            # O dicionário de transições original do automato recebe o 'novas_transicoes' para iniciar um proximo loop.
            self.transicoes = copy.deepcopy(novas_transicoes)

        # No fim do loop, vamos passar uma ultima vez pelo dicionário de transições, unificando quaisquer listas com mais de um valor sobressalentes,
        # transformando todas as listas em strings e checando quais estados possuem o estado final original, formando a nova lista de estados finais!
        estados_finais = []
        for estado in self.transicoes:
            for transicao in self.transicoes[estado]:
                transicao_lista = self.transicoes[estado][transicao]
                self.transicoes[estado][transicao] = ''.join(transicao_lista)
            for estado_final in self.estados_finais:
                if estado_final in estado:
                    if estado not in estados_finais:
                        estados_finais.append(estado)
        self.estados_finais = estados_finais

    def certificar_funcao_total(self):
        aux_transicoes = copy.deepcopy(self.transicoes)
        for estado in aux_transicoes:
            temp_alfabeto = copy.deepcopy(self.alfabeto)
            for letra in self.transicoes[estado]:
                temp_alfabeto.remove(letra)
            if temp_alfabeto:
                if not self.transicoes.get('aux'):
                    self.transicoes['aux'] = {}
                    for letra in self.alfabeto:
                        self.transicoes['aux'][letra] = f'aux'
                for letra in temp_alfabeto:
                    self.transicoes[estado][letra] = f'aux'

    def teste_palavra(self, palavra):
        if self.tipo == 'afn':
            self.converter_afn_afd()

        self.certificar_funcao_total()

        for letra in palavra:
            if letra not in self.alfabeto:
                print(
                    f'\nA palavra {palavra} não se enquadra no alfabeto definido.')
                return False

        estado_atual = self.estado_inicial

        for letra in palavra:
            estado_atual = (self.transicoes.get(
                estado_atual).get(letra))

        if estado_atual in self.estados_finais:
            print(f'\nA palavra {palavra} foi aceita.')
            return True
        else:
            print(f'\nA palavra {palavra} foi rejeitada.')
            return False
