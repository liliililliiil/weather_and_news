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

def scrape_news():
    print(" < Today's Hedaline News > ")
    url = "https://news.naver.com/main/ranking/popularDay.naver"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs = {"class" : "rankingnews_list"}).find_all("li")
    # for index, news in enumerate(news_list):
    #     title = news.find("a").get_text()
    #     link = news.find("a")["href"]
    #     print("{}. {}".format(index + 1, title))
    #     print(" 링크 : {}". format(link))
    
    news1 = news_list[0].find("a").get_text()
    news1_link = news_list[0].find("a")["href"]
    
    news2 = news_list[1].find("a").get_text()
    news2_link = news_list[1].find("a")["href"]
    
    news3 = news_list[2].find("a").get_text()
    news3_link = news_list[2].find("a")["href"]
    
    news4 = news_list[3].find("a").get_text()
    news4_link = news_list[3].find("a")["href"]
    
    news5 = news_list[4].find("a").get_text()
    news5_link = news_list[4].find("a")["href"]
    
scrape_news()