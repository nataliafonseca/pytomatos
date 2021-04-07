import json
import copy
from itertools import chain, combinations


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
        novo_estado_criado = True

        while novo_estado_criado:
            novas_transicoes = {}

            for estado in self.transicoes:
                novas_transicoes[estado] = {}
                for transicao in self.transicoes[estado]:
                    transicao_lista = self.transicoes[estado][transicao]
                    novas_transicoes[estado][transicao] = transicao_lista

            for estado in self.transicoes:
                for transicao in self.transicoes[estado]:
                    transicao_lista = self.transicoes[estado][transicao]
                    if len(transicao_lista) > 1:
                        novo_estado = ''.join(transicao_lista)
                        novas_transicoes[novo_estado] = {}
                        novas_transicoes[estado][transicao] = [novo_estado]

                        for letra in self.alfabeto:
                            for estado_ in transicao_lista:
                                if novas_transicoes[estado_].get(letra):
                                    if not novas_transicoes[novo_estado].get(letra):
                                        novas_transicoes[novo_estado][letra] = []
                                    already_in = False
                                    for item in novas_transicoes[novo_estado][letra]:
                                        if novas_transicoes[estado_][letra][0] in item:
                                            already_in = True
                                    if not already_in:
                                        novas_transicoes[novo_estado][letra] += novas_transicoes[estado_][letra]

            novo_estado_criado = len(novas_transicoes) > len(self.transicoes)
            self.transicoes = novas_transicoes

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
                self.transicoes[f'aux_{estado}'] = {}
                for letra in self.alfabeto:
                    self.transicoes[f'aux_{estado}'][letra] = f'aux_{estado}'
                for letra in temp_alfabeto:
                    self.transicoes[estado][letra] = f'aux_{estado}'

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
