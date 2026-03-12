from abc import ABC, abstractmethod
class Person(ABC):

    def __init__(self, person_id, name, surname, cell_number, email):
         self.person_id = person_id
         self.name = name
         self.surname = surname
         self.cell_number = cell_number
         self.email = email

    def display_info(self):
        print("ID:", self.person_id)
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Cell:", self.cell_number)
        print("Email:", self.email)

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def display_all(self):
        pass