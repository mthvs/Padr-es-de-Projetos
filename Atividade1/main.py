from Calcular_IR import Calculo
from Tipo_pessoa import TP
from PessoaFactory import pessoaFactory

if __name__ == "__main__":
    pessoaF = pessoaFactory.Pessoa(TP.pFisica)
    pessoaJ = pessoaFactory.Pessoa(TP.pJuridica)

    Calculo.Calcular_IR(pessoaF)
    print('')
    Calculo.Calcular_IR(pessoaJ)