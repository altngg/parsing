import requests

def get_vacancies():
    url = "https://api.hh.ru/vacancies?only_with_salary=true"
    params = {
        
        "per_page": 10,

    }
    headers = {
        "User-Agent": "Chrome",  
    }
    all_vacancy = list()
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
            all_vacancy.append([vacancy_title, vacancy_salary, vacancy_expirience, vacancy_area, vacancy_url])
    # else:
    #     print(f"Ошибка запроса: {response.status_code}")
    return all_vacancy 
# def main():
#     p = get_vacancies()


# get_vacancies("Программист")

if __name__ == "__jj__":
    get_vacancies()

# def search_vacancies():
#     keyword = input.input("Enter a keyword to search for vacancies:", type=input.TEXT)
#     output.clear()
#     output.put_text("Searching for vacancies...")
#     get_vacancies(keyword)


# def main():
#     keyword = input()
#     get_vacancies(keyword)


     
