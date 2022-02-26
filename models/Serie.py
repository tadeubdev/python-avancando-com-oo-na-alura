from models.Programa import Programa


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'A série {self.nome} foi lançada em {self.ano} e tem {self.temporadas} temporadas'
