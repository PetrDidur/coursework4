from api import HeadHunterAPI, SuperJobAPI


class Vacancy:
    __slots__ = ("title", "url", "salary", "description")

    def __init__(self, title, url, salary, description):
        self.title: str = title
        self.url: str = url
        self.salary: float = salary
        self.description: str = description

    def __str__(self) -> str:
        return f"{self.__class__.__name__} Название: {self.title}, Ссылка: {self.url}, Зарплата: {self.salary},Описание: {self.description}"

    def __repr__(self):
        return f"{self.__class__.__name__} Название: {self.title}, Ссылка: {self.url}, Зарплата: {self.salary}, Описание: {self.description}"

    def __lt__(self, other):
        return int(self.salary) < int(other.salary)

    def __le__(self, other):
        return int(self.salary) <= int(other.salary)

    def __gt__(self, other):
        return int(self.salary) > int(other.salary)

    def __ge__(self, other):
        return int(self.salary) >= int(other.salary)






