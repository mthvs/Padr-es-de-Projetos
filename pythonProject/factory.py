from Tipo_Npc import Npcs
from Dragao import dragao
from JOKER import Joker
from ANFITRIAO import Anfitriao


class NpcFactory():

    def Npc(tipo):
        if tipo == Npcs.Dragao:
            return dragao('Prometeus', 400, 40)
        elif tipo == Npcs.Joker:
            return Joker('joker', 200, 20)
        elif tipo == Npcs.Anfitriao:
            return Anfitriao('tomas', 40, 5)

