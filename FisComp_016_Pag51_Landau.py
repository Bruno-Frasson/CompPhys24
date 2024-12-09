# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:10:30 2024

@author: Bruno O. and Enzo C.
"""

# Escreva um código que calcula o valor do sen(x) até que o erro absoluto entre os termos da série seja menor que 1e-8

def fat(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return(fat)

def serie_sen(x_0):
  # Reduz x_0 ao intervalo [0, 2π]
  pi = 3.14159265
  x = x_0 % (2*pi)
  # Condições iniciais
  erro = 1e-8
  a = x
  S = 0
  n = 0
  # Somas Parciais
  while abs(a) > erro:
    A = S
    n += 1
    S += ((-1)**(n + 1))*(x**(2*n-1))/fat(2*n-1)
    a = S - A
    print(a)
    print(S)
  return print(f"sin({x_0}) = {S} \n")

# Testes
serie_sen(0)
serie_sen(1)
serie_sen(6)
serie_sen(10)
serie_sen(-10)