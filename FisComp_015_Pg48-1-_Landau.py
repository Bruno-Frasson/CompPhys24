# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:15:49 2024

@author: Enzoi C. e Bruno O.
"""

"""
1) Consider the 32-bit single-precision floating-point number A:
    
                s           e                         f
Bit position    31      30    23        22                         0
Value           0       0000 1110       1010 0000 0000 0000 0000 000

a) What are the (binary) values for the sign s, the exponent e, and the fractional
mantissa f ? (Hint: e10 = 14.)
b) Determine decimal values for the biased exponent e and the true exponent
p.
c) Show that the mantissa of A equals 1.625 000.
d) Determine the full value of A.

RESPOSTA:
    a)  Os valores são: s = 0; e = 0000 1110; f = 1010 0000 0000 0000 0000 000
    b) Convertendo e = 0000 1110 para decimal, temos:
        0000 1110 = 0 + ... + 0 + 2^3 + 2^2 + 2^1 + 0 = 8 + 4 + 2 = 14
       Sendo p = e - bias:
        p = e - 127 (single precision) --> p = 14 -127 = -113
    c) Pelo bit implícito (fantasma) = 1, temos:
        f = 1010 0000 0000 0000 0000 000
        f = 1*2^(-1) + 0*2^(-2) + 1*2(-3) + 0 + ... + 0 = 1/2 + 0 + 1/8 + 0
        f = 0.5 + 0.125 = 0.625
        Sendo a mantissa completa M = 1 + f (para numeros -- normais --):
            M = 1 + 0.625 = 1.625
    d) O valor completo de A é dado por:
        A = (-1)^(s)*1.f*2^(p) 
        A = (-1)^(0)*1.625*2^(-113)
        A = 1.625*2^(-113)
"""
