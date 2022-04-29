"""Programa que pega alguns dados do cliente e da a ele um desconto na comida favorita dele"""
import random

desconto = random.randint(10, 100)
name = input('Qual seu nome? ')
food = input('Sua comida fav? ')

def cliente(name, food, desconto):
    print(f'\nOla, {name}! seja bem vinde')
    print(f'Observamos aqui que a sua comida fav é {food}')
    print('E...')
    print(f'Voce acabou de ganhar um combo de {food}, com desconto de {desconto}%!!! ')

cliente(name, food, desconto)

