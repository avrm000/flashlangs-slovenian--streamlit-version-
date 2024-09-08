import streamlit as st
import csv
import json

with open('words2.csv', 'r', encoding = 'utf-8') as file: 

    reader = csv.reader(file)

    for riga in reader: 
        print(riga) 

