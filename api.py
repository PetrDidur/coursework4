from abc import ABC, abstractmethod

import requests


class Api(ABC):

    @abstractmethod
    def get_vacancies(self, text: str):
        pass


class HeadHunterAPI(Api):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies/"

    def get_vacancies(self, text: str):
        params = {
            "text": {text.lower()},
            "area": 1
        }
        vacancies = requests.get(self.url, params=params)
        return vacancies.json()


class SuperJobAPI(Api):
    def __init__(self):
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, keyword: str):
        headers = {
            "X-Api-App-Id": "v3.r.118187302.cddd647fa01a75e0a8bc90dd41f11ebc8752acdb.9aa73f5d1e50dcc11312ad742444c2eed695743d"
        }
        params = {
            "keyword": {keyword.lower()},
            "town": "Москва"
        }

        response = requests.get(self.url, headers=headers, params=params)
        data = response.json()
        return data




