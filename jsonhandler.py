import json
from abc import ABC, abstractmethod


class FileHandler(ABC):
    """
    Абстрактный класс для работы с файлами
    """
    @abstractmethod
    def add_vacancy(self, vacancy_data):
        pass

    @abstractmethod
    def get_vacancy(self, criteria):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        pass


class JsonHandler(FileHandler):
    """Класс наследуемый от абстрактного для работы с вакансиями HH.ru"""
    def __init__(self):
        self.file_path = "vacancy.json"

    def add_vacancy(self, vacancy_data):
        with open(self.file_path, 'a', encoding="utf-8") as file:
            json_str = json.dumps(vacancy_data, ensure_ascii=False)
            file.write(json_str + '\n')

    def get_vacancy(self, criteria):
        found_vacancies = []
        with open(self.file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            for i in data:
                if criteria in i['title']:
                    found_vacancies.append(i)
        return found_vacancies

    def remove_vacancy(self, criteria):
         updated_vacancies = []
         with open(self.file_path, 'r', encoding="utf-8") as file:
             data = json.load(file)
             for i in data:
                 if criteria.lower() not in i["title"].lower():
                     updated_vacancies.append(i)

         with open(self.file_path, 'a', encoding='utf-8') as f:
             json_str = json.dumps(updated_vacancies, ensure_ascii=False)
             f.write((json_str + '\n'))







