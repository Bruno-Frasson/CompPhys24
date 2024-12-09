# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:41:44 2024

@author: User
"""

# 2) Write a program that determines the underflow and overflow limits (within
# a factor of 2) for Python on your computer. Here is a sample pseudocode

under = 1
over = 1
run = 0


while True:    # Mais prático que usar laço for
    try:   
        underflow = under / 2
        overflow = over * 2
        
        if underflow == 0:
            print(f"Underflow detectado na iteração {run}!")
            break  
        
        if overflow == float('inf'):
            print(f"Overflow detectado na iteração: {run}!")
            break
        
        under = underflow
        over = overflow
        run += 1
        print(run, overflow)
    except ValueError:
        print(f"Overflow detectado na iteração: {run}!")
        break
"""
Para float's, overflow ocorre na iteração 1023 e underflow na iteração 1074
Para int's, overflow ocorre na iteração 14285 (???) e underflow na iteração 1074
"""
