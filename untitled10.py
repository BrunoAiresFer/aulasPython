# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sd1aTYRK28bMznJijuv5hkLKpgHnIK6w
"""

#Atividade 1

televisor = 4400
tempo = 3
mes = 30
consumo = (televisor / 1000) * tempo * mes
pessoa = 6 
consumo = (televisor / 1000) * tempo * mes * pessoa
print(f"O consumo mensal do televisor é de: {round(consumo, 2 )} kwh")

#Atividade 2

televisor = 200
tempo = 6 
mes = 30
consumo = (televisor / 1000) * tempo * mes

print(f"O consumo mensal do televisor é de: {round(consumo, 2 )} kwh")

#Atividade 3

incadescente = 100
fluorescente = 20
uso = 5 
mes = 30
preco_kwh = 0.40

incadescente = (incadescente / 1000) * uso * mes * preco_kwh
fluorescente = (fluorescente / 1000) * uso * mes * preco_kwh
economia = incadescente - fluorescente
economia = economia * preco_kwh
print(f"A economia mensal proporcionada é de: R$ {round(economia, 2)}")

#Atividade 4

fluorescente = 15
incadescente = 60
hora = 1 

kwh_gastos_f = fluorescente * hora
kwh_gastos_i = incadescente * hora

economia = kwh_gastos_i - kwh_gastos_f

print(f"A economia com a troca foi de: {round(economia, 2)}kWh.")