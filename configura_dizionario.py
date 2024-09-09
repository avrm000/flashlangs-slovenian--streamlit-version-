
from helpers import Helpers

class Configura_dizionario: 


    def __init__(self): 

        pass

    def trasforma_values_in_list(self, dizionario):

        nuovo_dizionario = {}

        for key in dizionario.keys(): 

            nuovo_dizionario[key] = [dizionario[key]]

        return nuovo_dizionario
    
    def aggiungi_probs_al_dizionario(self, dizionario_di_liste, mode):

        if mode == 'normal': 
            
            lunghezza = len(dizionario_di_liste)
            lista_esponenziale_inversa = Helpers().esponenziale_inverso(lunghezza)

            for indice, key in enumerate(dizionario_di_liste.keys()): 
                
                dizionario_di_liste[key].append(lista_esponenziale_inversa[indice])

            return [dizionario_di_liste, lista_esponenziale_inversa]


    

        

    
