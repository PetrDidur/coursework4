import json

from api import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy
from jsonhandler import JsonHandler

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

search_name = "Python"

data_hh = hh_api.get_vacancies(search_name)
#print(data_hh)

data_sj = superjob_api.get_vacancies(search_name)
#print(data_sj)

vacancies_data = []
for i in data_hh.get('items', []):
    title = i.get('name', ' ')
    link = i.get('alternate_url', '')
    salary = i.get('salary')
    description = i.get('snippet', {}).get('responsibility', '')
    vacancies_data.append({'title': title, 'link': link, 'salary': salary, 'description': description})

for i in data_sj.get('objects', []):
    title = i.get('profession', ' ')
    link = i.get('link', '')
    salary = i.get('payment_from', 'payment_to')
    description = i.get('description')
    vacancies_data.append({'title': title, 'link': link, 'salary': salary, 'description': description})


vacancies = []
for item in vacancies_data:
    vacancy = Vacancy(item['title'], item['link'], item['salary'], item['description'])
    vacancies.append(vacancy)

vacancies_to_json = [vacancy.to_json() for vacancy in vacancies]
print(vacancies_to_json)

jsonhandler = JsonHandler()
#jsonhandler.add_vacancy(vacancies_to_json)

print(jsonhandler.get_vacancy("Junior"))
jsonhandler.remove_vacancy("Стажер")


