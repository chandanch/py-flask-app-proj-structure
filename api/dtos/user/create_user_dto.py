# app/dto/task_dto.py
class CreateUserDTO:
    def __init__(self, name, biopic, country):
        self.name = name
        self.biopic = biopic
        self.country = country
