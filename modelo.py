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


vingadores = Filme('Vingadores', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)
