# -*- coding: utf-8 -*-

import random

def __init__(giris):
    try:
        return str(eval(giris))
    except(SyntaxError):
        return random.choice(['Verecek cevap bulamadım.', 'Daha anlaşılabilir bir şey söylesen?'])