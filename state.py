from pages.liturgia import create_liturgia
from pages.oracoes import create_oracoes
from pages.devocoes_carismas import create_devocoes_carismas
from pages.calendario import create_calendario
from pages.contatos import create_contatos

# Containers globais para manter o estado
liturgia = create_liturgia()
oracoes = create_oracoes()
devocoes_carismas = create_devocoes_carismas()
calendario = create_calendario()
contatos = create_contatos()

