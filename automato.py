import json
import copy


class Automato:
    def __init__(self, automato_json):
        self.automato_json = automato_json
        self.automato = self.ler_json(automato_json)
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

    def converter_afn_afd(self):
        return

    def teste_palavra(self, palavra):
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
