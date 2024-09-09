
import math
import numpy as np

class Helpers: 


    def __init__(self): 

        pass

    def esponenziale_inverso(self, lunghezza_array): 

        array = np.linspace(1, 0, lunghezza_array)
        
        array = np.exp(array)

        return array    

    def prendi_probs(self, dizionario): 

        probs = []

        for key, value in dizionario.items(): 

            probs.append(value[1])


        return probs
    



