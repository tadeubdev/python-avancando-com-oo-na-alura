from abc import abstractmethod


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

    @abstractmethod
    def __str__(self):
        pass
