from Tipo_pessoa import TP
from pessoa_fisica import PF
from Pessoa_juridica import PJ

class Calculo():

    def Calcular_IR(tipo):
        if  tipo.__class__ == PJ:
            IR = tipo.renda*0.15
            print('Nome:',tipo.nome)
            print('CNPJ:',tipo.cnpj)
            print('Renda:',tipo.renda)
            print('Imposto de Renda',IR)
            return IR
        elif tipo.__class__== PF:
            IR = tipo.renda * 0.15
            print('Nome:',tipo.nome)
            print('CPF:',tipo.cnpj)
            print('Renda:',tipo.renda)
            print('Imposto de Renda',IR)
            return IR