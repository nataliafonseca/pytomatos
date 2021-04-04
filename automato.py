import json


class Automato:
    def __init__(self, automato_json):
        self.automato_json = automato_json
        self.automato = self.ler_json(automato_json)
        self.alphabet = self.automato['alphabet']
        self.initial_state = self.automato['initial_state']
        self.final_state = self.automato['final_state']
        self.transitions = self.automato['transitions']

    def __repr__(self):
        with open(self.automato_json) as file:
            lines = file.readlines()
            count = 0
            string = ''
            for line in lines:
                count += 1
                string += line
        return string

    @staticmethod
    def ler_json(automato_json):
        with open(automato_json) as json_file:
            data = json.load(json_file)
            return data




