# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Hl5zlC-_ogpqSfhYAJ-UF4lXbF-8SSO
"""

#Atividade 5

#Questão 1

tv = 200
horas = 3
dias = int(input("Quantos dias foi utilizado a tv?: "))

kwh_mensal = (tv * horas * dias)/100

print(kwh_mensal)

#Questão 2

num = float(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print(f'O dobro é: {dobro}. O triplo é: {triplo}. A raiz é: {raiz}')

#Questão 3

nome = str(input('Seu nome: '))
idade = int(input("Sua idade: "))
peso = float(input('Seu peso: '))

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Peso: {peso}')

#Questão 4

nome = str(input("Seu nome: "))

print(f"Seja muito bem-vindo(a) {nome} a Funec Riacho!")

#Questão 5

preco = float(input('Preço do produto: '))
desconto = preco * 0.05
desconto = preco - desconto
print(f'O preço do produto é: {desconto}')

#Questão 6

raio = float(input('Digite o raio do círculo: '))
area = 3.14 * raio * raio
print(f"A area do círculo é: {area}")

#Questão 7

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))

soma = valor1 + valor2
print(f"Soma é:{soma} ")

multiplicacao = valor1 * valor2
print(f"Multiplicação é: {multiplicacao}")

div = valor1 / valor2
print(f"Divisão é: {div}")

div_int = valor1 // valor2
print(f'A divisão inteira é: {div_int}')

potencia = valor1 ** valor2
print(f'A potência é: {potencia}')