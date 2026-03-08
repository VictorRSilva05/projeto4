import datetime
import random
import string

def data_atual():
    return datetime.date.today()

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

import random
import string

def gerar_senha(tamanho=10):
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha