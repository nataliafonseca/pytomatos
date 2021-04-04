import json


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
        string += f'Estado Final: {self.estados_finais}\n'
        string += f'Transições: \n'
        for chave, valor in self.transicoes.items():
            string += f'    {chave}: {valor}\n'
        return string

    @staticmethod
    def ler_json(automato_json):
        with open(automato_json) as json_file:
            dicionario = json.load(json_file)
            return dicionario

    def teste_palavra(self, palavra):
        for letra in palavra:
            if letra not in self.alfabeto:
                print(
                    f"\nA palavra {palavra} não se enquadra no alfabeto definido.")
                return False

        estado_atual = self.estado_inicial

        for letra in palavra:
            estado_atual = (self.transicoes.get(
                estado_atual).get(letra))

        if estado_atual in self.estados_finais:
            print(f"\nA palavra {palavra} foi aceita.")
            return True
        else:
            print(f"\nA palavra {palavra} foi rejeitada.")
            return False
