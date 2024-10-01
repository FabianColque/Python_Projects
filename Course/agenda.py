from person import Person
from datetime import date

class Agenda:
    def __init__(self):
        self.__contatos : list[Person] = []

    @property
    def contatos(self) -> list[Person]:
        return self.__contatos
    
    def armazenar_contatos(self, contato:Person) -> None:
        self.contatos.append(contato)

    def remover_contato(self, contato : Person) -> None:
        self.contatos.remove(contato)

    def buscar_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.name == nome:
                print(f'O contato {nome} está nessa posiçao {indice}')

    def print_agenda(self) -> None:
        for contato in self.contatos:
            contato.print()

    def print_contato(self, indice: int)->None:
        self.contatos[indice].print()

if __name__ == '__main__':
    contato1: Person = Person('Fabian', date(1992, 2, 19), 'fbcolque@gmail.com')
    contato2: Person = Person('Ernesto', date(1992, 2, 20), 'ernesto@gmail.com')
    contato3: Person = Person('Colque', date(1992, 2, 21), 'colque@gmail.com')

    agenda: Agenda = Agenda()
    agenda.armazenar_contatos(contato1)
    agenda.armazenar_contatos(contato2)
    agenda.armazenar_contatos(contato3)

    agenda.print_agenda()
    agenda.buscar_contato('Fabian')
    agenda.print_contato(2)
    agenda.remover_contato(contato3)
    agenda.print_agenda()