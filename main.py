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
            search_name = input("Enter your request ")
            hh_api = HeadHunterAPI()
            data_hh = hh_api.get_vacancies(search_name)
            if not data_hh:
                print("No vacancies")
            else:
                filtered_data_hh = [item for item in data_hh if item.get('salary') is not None]
                sorted_data = sorted(filtered_data_hh, key=lambda x: x['salary']['from'] if x['salary']['from'] else 0, reverse=True)
                top_n = int(input("Enter the number of displayed vacancies "))
                top_n_data = sorted_data[:top_n]
                for item in top_n_data:
                    print(f" "
                          f"Название: {item['title']}\n"
                          f"Ссылка на вакансию: {item['link']}\n"
                          f"Зарплата от: {item['salary']['from']}\n"
                          f"Описание вакансии: {item['description']}\n"
                          f" ")
        elif platform == '2':
            search_name = input("Enter your request ")
            sj_api = SuperJobAPI()
            data_sj = sj_api.get_vacancies(search_name)
            if not data_sj:
                print("No vacancies")
            else:
                filtered_data_sj = [item for item in data_sj if item.get('salary') is not None]
                sorted_data = sorted(filtered_data_sj, key=lambda x: x['salary'] if x['salary'] else 0, reverse=True)
                top_n = int(input("Enter the number of displayed vacancies "))
                top_n_data = sorted_data[:top_n]
                for item in top_n_data:
                    print(f" "
                          f"Название: {item['title']}\n"
                          f"Ссылка на вакансию: {item['link']}\n"
                          f"Зарплата от: {item['salary']}\n"
                          f"Описание вакансии: {item['description']}\n"
                          f" ")
        elif platform == '3':
            print("Thank you! Come again")
            break
        else:
            print('There is no such an option!')


user_interaction()






