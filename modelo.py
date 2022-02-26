from models.Filme import Filme
from models.Playlist import Playlist
from models.Serie import Serie

vingadores = Filme('Vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

flash = Serie('Flash', 2017, 6)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, tmep, demolidor]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

vingadores.nome = 'Vingadores: Ultimato'
playlist_fim_de_semana[0] = vingadores

print(f'Tamanho da playlist "{playlist_fim_de_semana.nome}": '
      f'{len(playlist_fim_de_semana)} programas.\n')

for programa in playlist_fim_de_semana:
    print(programa)

print('')

print(playlist_fim_de_semana.programa_esta_na_lista(vingadores))

print(playlist_fim_de_semana.programa_esta_na_lista(flash))
