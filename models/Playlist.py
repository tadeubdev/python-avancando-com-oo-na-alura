from models import Serie


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
