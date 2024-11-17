from cgitb import text
from email import header
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    def create_soup(url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
        res = requests.get(url, headers=headers) 
        res.raise_for_status() 
        soup = BeautifulSoup(res.text, "lxml")
        return soup
    

    @app.route('/')
    def scrape_weather():
        
        url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8" # 날씨정보 url    
        soup = create_soup(url)
        url_news = "https://news.naver.com/main/ranking/popularDay.naver"
        soup_news = create_soup(url_news)
        # 현재 온도, 기상 상황, 최저기온, 최고기온
        def current_temp():
            current_temp = soup.find("div", attrs = {"class" : "temperature_text"}).get_text() # 현재기온
            return current_temp
        
        def cast():
            cast = soup.find("p", attrs = {"class" : "summary"}).get_text() # 어제와 온도 비교 & 기상상황
            return cast
        
        def rain():
            rain = soup.find("dl", attrs = {"class" : "summary_list"}).get_text() # 강수확률, 습도, 풍향, 풍속
            return rain
        
        def rain_morning():
            rain_morning = soup.find("span", attrs = {"class" : "weather_inner"}) # 오전 오후 강수확률
            return rain_morning
        
        def rain_afternoon():
            rain_afternoon = rain_morning().next_sibling.next_sibling
            return rain_afternoon
        
        def min_temp():
            min_temp = soup.find("span", attrs = {"class" : "lowest"}).get_text() # 최저기온
            return min_temp
        
        def max_temp():
            max_temp = soup.find("span", attrs = {"class" : "highest"}).get_text() # 최고기온
            return max_temp
        
        # 대기정보
        def atmosphere():
            atmosphere = soup.find("ul", attrs = {"class" : "today_chart_list"})
            return atmosphere
        
        
        
        
        # weather_dic = {"current_temp" : current_temp(),
        #                "cast" : cast(),
        #                "min_temp" : min_temp(),
        #                "max_temp" : max_temp(),
        #                "rain" : rain(),
        #                "rain_morning" : rain_morning().get_text(),
        #                "rain_afternoon" : rain_afternoon().get_text(),
        #                "atmosphere" : atmosphere().get_text(),
        #                "fine_dust" : fine_dust().get_text(),
        #                "ultra_fine_dust" : ultra_fine_dust().get_text(),
        #                "uv" : uv().get_text(),
        #                "sunset" : sunset().get_text()}
        # 현재 온도, 기상 상황, 최저기온, 최고기온, 오전 오후 강수확률
        # print(current_temp())
        # print(cast())
        # print(min_temp(), "/", max_temp())
        # print(rain())
        # print("{} / {}".format(rain_morning().get_text(), rain_afternoon().get_text()))
        
        # # 대기정보
        # print("{} / {} / {} / {}".format(fine_dust().get_text(), ultra_fine_dust().get_text(), uv().get_text(), sunset().get_text()))
        현재기온 = current_temp()
        기상 = cast()
        최저기온=min_temp()
        최대기온=max_temp()
        강수확률=rain()
        오전강수량=rain_morning().get_text()
        오후강수량=rain_afternoon().get_text()
        대기상황=atmosphere().get_text()
        
        
        news_list = soup_news.find("ul", attrs = {"class" : "rankingnews_list"}).find_all("li")
        
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
        
        
        return render_template('index.html',현재기온 = 현재기온, 기상 = 기상 ,최저기온=최저기온, 최대기온=최대기온, 강수확률=강수확률, 오전강수량=오전강수량, 오후강수량=오후강수량
                            ,뉴스1 = news1, 뉴스1링크 = news1_link, 뉴스2=news2, 뉴스2링크=news2_link, 뉴스3=news3, 뉴스3링크=news3_link, 뉴스4=news4, 뉴스4링크=news4_link, 뉴스5=news5, 뉴스5링크=news5_link)
    return app

        
    
        
# if __name__ == "__main__":
#     app.run(debug=True)