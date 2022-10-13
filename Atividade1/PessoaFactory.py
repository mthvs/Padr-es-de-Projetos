from Pessoa_juridica import  PJ
from pessoa_fisica import PF
from Tipo_pessoa import TP

class pessoaFactory:

    def Pessoa(tipo):
        if tipo == TP.pFisica:
            return PF('Matheus', '115.710.459-33', 12500.00)
        elif tipo == TP.pJuridica:
            return PJ('Manuel', '00.112.112/0001-39', 1250320.00)