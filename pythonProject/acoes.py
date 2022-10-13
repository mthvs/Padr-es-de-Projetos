from Npc import NPC

class Acoes(NPC):

 def atacar(np2, np1):
        dano = np1.saude - np2.forca
        print(f'{np1.nome} foi atacado por' , np2.nome)
        print(f'{np1.nome} sofreu', np2.forca,'pontos de dano')
        np1.saude = dano
        print(f'a vida atual do {np1.nome} é', np1.saude)
        pass