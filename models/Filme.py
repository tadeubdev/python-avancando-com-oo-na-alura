from models.Programa import Programa


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'O filme {self.nome} foi lançado em {self.ano} e tem {self.duracao} minutos de duração'
