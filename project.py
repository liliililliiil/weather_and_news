from cgitb import text
from email import header
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    res = requests.get(url, headers=headers) 
    res.raise_for_status() 
    soup = BeautifulSoup(res.text, "lxml")
    return soup
    

def scrape_weather():
    print(" < Today's weather > ")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8" # 날씨정보 url    
    soup = create_soup(url)
    # 현재 온도, 기상 상황, 최저기온, 최고기온
    current_temp = soup.find("div", attrs = {"class" : "temperature_text"}).get_text() # 현재기온
    cast = soup.find("p", attrs = {"class" : "summary"}).get_text() # 어제와 온도 비교 & 기상상황
    rain = soup.find("dl", attrs = {"class" : "summary_list"}).get_text() # 강수확률, 습도, 풍향, 풍속
    rain_morning = soup.find("span", attrs = {"class" : "weather_inner"}) # 오전 오후 강수확률
    rain_afternoon = rain_morning.next_sibling.next_sibling
    min_temp = soup.find("span", attrs = {"class" : "lowest"}).get_text() # 최저기온
    max_temp = soup.find("span", attrs = {"class" : "highest"}).get_text() # 최고기온
    
    # 대기정보
    atmosphere = soup.find("ul", attrs = {"class" : "today_chart_list"})
    fine_dust = atmosphere.find("li", attrs = {"class" : "item_today level1"}) # 미세먼지
    
    ultra_fine_dust = fine_dust.next_sibling.next_sibling # 초미세먼지
    uv = ultra_fine_dust.next_sibling.next_sibling # 자외선
    sunset = uv.next_sibling.next_sibling # 일몰
    
    # 현재 온도, 기상 상황, 최저기온, 최고기온, 오전 오후 강수확률
    print(current_temp)
    print(cast)
    print(min_temp, "/", max_temp)
    print(rain)
    print("{} / {}".format(rain_morning.get_text(), rain_afternoon.get_text()))
    
    # 대기정보
    print("{} / {} / {} / {}".format(fine_dust.get_text(), ultra_fine_dust.get_text(), uv.get_text(), sunset.get_text()))
    


def scrape_news():
    print(" < Today's Hedaline News > ")
    url = "https://news.naver.com/main/ranking/popularDay.naver"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs = {"class" : "rankingnews_list"}).find_all("li")
    for index, news in enumerate(news_list):
        title = news.find("a").get_text()
        link = news.find("a")["href"]
        print("{}. {}".format(index + 1, title))
        print(" 링크 : {}". format(link))
    
if __name__ == "__main__":
    # scrape_weather()
    scrape_news()