from Tipo_Npc import Npcs
from Dragao import dragao
from JOKER import Joker
from ANFITRIAO import Anfitriao
from factory import NpcFactory
from Tipo_Npc import Npcs
from acoes import Acoes

if __name__ == "__main__":
   dragao1 = NpcFactory.Npc(Npcs.Dragao)
   joker = NpcFactory.Npc(Npcs.Joker)

   Acoes.atacar(dragao1,joker)
   print('')
   Acoes.atacar(joker,dragao1)


