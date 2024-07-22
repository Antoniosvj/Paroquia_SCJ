#https://github.com/Dancrf/liturgia-diaria
import requests
import json

#dia=30
#mes=6

liturgia = requests.get('https://liturgiadiaria.site/') #liturgia do dia
#liturgia = requests.get(f"https://liturgiadiaria.site/?dia={dia}&mes={mes}") #liturgia do dia especifico

liturgia = liturgia.json()
#print(liturgia)

data = liturgia['data']
print(data)
liturgia_dia= liturgia['liturgia']
print(liturgia_dia)
cor = liturgia['cor']
print(cor)
dia = liturgia['dia']
print(dia)
primeira_leitura = liturgia['primeiraLeitura']
print(primeira_leitura)
salmo = liturgia['salmo']
print(salmo)
segunda_leitura = liturgia['segundaLeitura']
print(segunda_leitura)
evangelho = liturgia['evangelho']
print(evangelho)