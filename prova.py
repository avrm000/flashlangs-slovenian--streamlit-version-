import streamlit as st
import json
from dizionario import Dizionario
import random
from helpers import Helpers 



with open('database_copy.json', 'r', encoding = 'utf-8') as file: 

    dizionario = json.load(file)
    
    print('operazione andata a buon fine')



oggetto_dizionario = dizionario

probs = Helpers().prendi_probs(oggetto_dizionario)





st.title('FASTLANGS.COM')






lista_parole_inglesi = list(oggetto_dizionario.keys())


scelta = random.choices(lista_parole_inglesi, probs)[0]



with st.expander(scelta):
    st.write(oggetto_dizionario[scelta][0])


positive = st.button('I know it')


negative = st.button('I dont know it')

if positive: 
    
     
    oggetto_dizionario[st.session_state.scelta][1] /= 500
     
    with open('database_copy.json', 'w', encoding = 'utf-8') as file: 
        json.dump(oggetto_dizionario, file, ensure_ascii=False, indent=4)
    

if negative and scelta != False:
  
     
    oggetto_dizionario[st.session_state.scelta][1] *= 1000
     
    with open('database_copy.json', 'w', encoding = 'utf-8') as file: 
        json.dump(oggetto_dizionario, file, ensure_ascii=False, indent=4)
  


 
st.session_state.scelta = scelta





