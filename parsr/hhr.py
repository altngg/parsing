from bs4 import BeautifulSoup
import requests
import fake_useragent
import time


def get_links(text):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=f"https://hh.ru/search/vacancy?text={text}&from=suggest_post&salary=&ored_clusters=true&area=1&page=1",
        headers={'user-agent':ua.random}   
    )          
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")
    try:
        page_num = int(soup.find("div", attrs={"class": "pager"}).find_all("span", recursive=False)[-1].find("a").find("span").text)
    except:
        return
    for page in range(page_num):
        try:
            data = requests.get(
            url=f"https://hh.ru/search/vacancy?text={text}&from=suggest_post&salary=&ored_clusters=true&area=1&page={page}",
            headers={'user-agent':ua.random}   
            )    
            if data.status_code != 200:
                continue
            soup = BeautifulSoup(data.content, "lxml")
            for a in soup.find_all("span", attrs={"сlass": "serp-item__title-link-wrapper"}).find("a", attrs={'class': 'bloko-link'}):
                yield f'https://hh.ru{a.attrs["href"].split("?")[0]}'
        except Exception as e:
            print(f"{e}")
        time.sleep(1)
    



def get_vacancies(link):
    pass

if __name__ == "__main__":
    for a in get_links("python"):
        print(a)