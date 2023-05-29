import json

from api import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy
from jsonhandler import JsonHandler


def user_interaction():
    """
    Функция осуществляет взаимодействие с пользователем
    :return:
    """
    while True:
        print("Hello!")
        platform = input("Choose the platform: 1) HeadHunter 2) SuperJob 3) Exit ")
        if platform == '1':
            search_name_hh = input("Enter your request ")
            hh_api = HeadHunterAPI()
            data_hh = hh_api.get_vacancies(search_name_hh)
            if not data_hh:
                print("No vacancies")
            else:
                filtered_data_hh = [item for item in data_hh if item.get('salary') is not None]
                sorted_data = sorted(filtered_data_hh, key=lambda x: x['salary']['from'] if x['salary']['from'] else 0, reverse=True)
                top_n = int(input("Enter the number of displayed vacancies "))
                top_n_data = sorted_data[:top_n]
                list_vacancies = []
                for item in top_n_data:
                    vacancy = Vacancy(item['title'], item['link'], item['salary']['from'], item['description'])
                    list_vacancies.append(vacancy)
                for vacancy in list_vacancies:
                    print(f" \n"
                          f"Название: {vacancy.title}\n"
                          f"Ссылка на вакансию: {vacancy.url}\n"
                          f"Зарплата от: {vacancy.salary}\n"
                          f"Описание вакансии: {vacancy.description}\n"
                          f" ")
                else:
                    return
        elif platform == '2':
            search_name_sj = input("Enter your request ")
            sj_api = SuperJobAPI()
            data_sj = sj_api.get_vacancies(search_name_sj)
            print(data_sj)
            if not data_sj:
                print("No vacancies")
            else:
                filtered_data_sj = [item for item in data_sj if item.get('salary') is not None]
                sorted_data = sorted(filtered_data_sj, key=lambda x: x['salary'] if x['salary'] else 0, reverse=True)
                top_n = int(input("Enter the number of displayed vacancies "))
                top_n_data = sorted_data[:top_n]
                list_vacancies = []
                for item in top_n_data:
                    vacancy = Vacancy(item['title'], item['link'], item['salary'], item['description'])
                    list_vacancies.append(vacancy)
                for vacancy in list_vacancies:
                    print(f" \n"
                          f"Название: {vacancy.title}\n"
                          f"Ссылка на вакансию: {vacancy.url}\n"
                          f"Зарплата от: {vacancy.salary}\n"
                          f"Описание вакансии: {vacancy.description}\n"
                          f" ")
                data_json = input("Want to save data in json?")
                if data_json == "yes":
                    jsonhandler = JsonHandler
                    jsonhandler.add_vacancy(list_vacancies)
                else:
                    return
        elif platform == '3':
            print("Thank you! Come again")
            break
        else:
            print('There is no such an option!')