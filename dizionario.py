import json
from configura_dizionario import Configura_dizionario as Conf

class Dizionario: 

    def __init__(self, dicti): 

        self.dicti = Conf().trasforma_values_in_list(dicti)
        self.dicti, self.probs = Conf().aggiungi_probs_al_dizionario(self.dicti, 'normal')

        
with open('words.json', 'r', encoding = 'utf-8') as file: 

    dizionario = json.load(file)

oggetto_dizionario = Dizionario(dizionario)

print(oggetto_dizionario.probs)
