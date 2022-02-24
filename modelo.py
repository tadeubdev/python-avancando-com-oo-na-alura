class Programa:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, likes):
        self.__likes = likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'O filme {self.nome} foi lançado em {self.ano} e tem {self.duracao} minutos de duração'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'A série {self.nome} foi lançada em {self.ano} e tem {self.temporadas} temporadas'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    def __setitem__(self, key, value):
        self.__programas[key] = value

    def __getitem__(self, item):
        return self.__programas[item]

    def __len__(self):
        return len(self.__programas)

    def programa_esta_na_lista(self, progr_selecionado):
        tipo_do_programa = 'A série' if type(progr_selecionado) == Serie else 'O filme'
        nome_programa = progr_selecionado.nome
        esta_na_lista = 'está' if progr_selecionado in self else 'não está'
        playlist_nome = self.nome

        return f'{tipo_do_programa} {nome_programa} {esta_na_lista} '\
               f'dentro da playlist {playlist_nome}.'


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
