import requests
from pywebio import input, output, start_server


def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies?only_with_salary=true"
    params = {
        "text": keyword,
        "area": 1,  # Specify the desired area ID (1 is Moscow)
        "per_page": 10,  # Number of vacancies per page
    }
    headers = {
        "User-Agent": "Your User Agent",  # Replace with your User-Agent header
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        num_vacancies = len(vacancies)

        if num_vacancies > 0:
            for i, vacancy in enumerate(vacancies):

                vacancy_title = vacancy.get("name")
                vacancy_area = vacancy.get("area",{}).get("name")
                vacancy_salary = vacancy.get("salary",{}).get("from")
                vacancy_expirience = vacancy.get("experience",{}).get("name")
                vacancy_url = vacancy.get("alternate_url")
                
                output.put_text(f"Название: {vacancy_title}")
                output.put_text(f"Город: {vacancy_area}")
                output.put_text(f"Зарплата: {vacancy_salary}")
                output.put_text(f"Опыт работы: {vacancy_expirience}")
                output.put_text(f"Ссылка на вакансию: {vacancy_url}")
                output.put_text("")  # Add an empty line for separation

                if i < num_vacancies - 1:
                    output.put_text("---------")  # Add separation line
        else:
            output.put_text("Вакансий не найдено.")
    


def search_vacancies():
    keyword = input.input("Введите ключевое слово для поиска:", type=input.TEXT)
    output.clear()
    output.put_text("Поиск вакансий...")
    get_vacancies(keyword)


if __name__ == '__hz__':
    start_server(search_vacancies, debug=True, port=8080, remote_access=True)