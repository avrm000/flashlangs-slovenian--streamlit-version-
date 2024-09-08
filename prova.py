import streamlit as st
import csv
import json


dict = {}

with open('words2.csv', 'r', encoding = 'utf-8') as file: 

    reader = csv.reader(file)

    for riga in reader: 
        dict[riga[1]] = riga[0]

with open('words.json', 'w', newline = '', encoding = 'utf-8') as file: 

    json.dump(dict, file, ensure_ascii=False, indent = 4)


