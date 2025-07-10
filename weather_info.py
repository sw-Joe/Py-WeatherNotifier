import requests
import BeautifulSoup

from io_func import read_json
from value import PATH_KEY


# Naver "오늘 서울 날씨" searchedWeatherInfo
nav_search_URL: str = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=오늘+서울+날씨&qdt=0&ie=utf8&query=오늘+서울+날씨"

basic_info = requests.get(nav_search_URL)
parsing = BeautifulSoup(basic_info.text, "html.parser")
NAVER_WEATHER_INFO = parsing.select_one(
    "div.temperature_text").text.replace("현재 온도", "")


# OpenWeather api weatherInfo

city_name: str = "seoul"
key_OW = read_json(PATH_KEY, "openWeather_api_key")
lang_code: str = "kr"

open_wthr_URL: str = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key_OW}&lang={lang_code}&units=metric"

# open_wthr = requests.get(open_wthr_URL).text
# OW_json = json.loads(open_wthr)
OW_json = requests.get(open_wthr_URL).json()
# print(OW_json)

OW_WEATHER_INFO = str(OW_json["main"]["temp"]) + "°"
icon_code = str(OW_json["weather"][0]["icon"])
# list indices must be integers or slices, not str

OW_Weather_icon = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

'''
    OW_dic_wthr = OW_json["weather"][0]
    기온_일반 = str(OW_json["main"]["temp"])
    기온_체감 = str(OW_json["main"]["feels_like"])
    기온_최저 = str(OW_json["main"]["temp_min"])
    기온_최대 = str(OW_json["main"]["temp_max"])
'''
