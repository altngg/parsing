# from typing import Any
import requests

# from django.core.management.base import BaseCommand
# from first.parcing.models import Vacancy 

def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies?only_with_salary=true"
    params = {
        "text": keyword,
        "per_page": 10,

    }
    headers = {
        "User-Agent": "Chrome",  
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            vacancy_area = vacancy.get("area",{}).get("name")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            vacancy_salary = vacancy.get("salary",{}).get("from")
            vacancy_expirience = vacancy.get("experience",{}).get("name")
            all_vacancy = (f"Название: {vacancy_title}\nЗарплата: {vacancy_salary}\nОпыт работы: {vacancy_expirience}\nГород: {vacancy_area}\nURL: {vacancy_url}\n")
        # else:
        #     print(f"Ошибка запроса: {response.status_code}")
     


if __name__ == "__main__":
    keyword = input()
    get_vacancies(keyword)



# class Command(BaseCommand):
#     help = 'Парсинг hh'

#     def handle(self, *args, **options):
#         p = 