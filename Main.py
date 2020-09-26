# # # Objetivos:
# # # Obtener data de MyAnimeList sobre anime de este año
# # # Haremos una playlist de youtube basado en esto
# - - - - - - - - - - Imports - - - - - - - - - -
import re, time
import datetime as dt
import pandas as pd
from bs4 import BeautifulSoup
from webbot import Browser
from selenium import webdriver


# - - - - - - - - - - Set-up - - - - - - - - - -
time_start = time.time()
time_load_search = 3
time_load_article = 2
date_today = dt.date.today()
# data frame & browser
db = pd.DataFrame(columns=["anime_title",
                           "anime_link",
                           "anime_op_list",
                           "anime_ed_list"])
link_base = 'https://myanimelist.net/topanime.php?type=airing'


# - - - - - - - - - - Webbot Navigation - - - - - - - - - -
web = Browser()
web.go_to(link_base)
time.sleep(time_load_search)
content = web.get_page_source() #Saca la código fuente de la página
soup = BeautifulSoup(content, 'html.parser') #Acá le defino a soup que lo que estoy viendo es un HTML

ranking_lists = soup.find_all("tr", {"class": "ranking-list"})

for anime in ranking_lists:
    # title, link
    anime_title = anime.find("div", {"class": "di-ib"}).getText()
    anime_link = anime.find("div", {"class": "di-ib"}).find("a")["href"]
    # - - - anime page
    web.go_to(anime_link)
    time.sleep(time_load_article)
    anime_content = web.get_page_source()
    anime_soup = BeautifulSoup(anime_content, 'html.parser')
    anime_op_list = []
    anime_ed_list = []
    # opening/ending theme
    for song_list in anime_soup.find_all("div", {"class": "opnening"}):
        for song in song_list.find_all("span"):
            song_cleaned = re.sub("^#\d{1,2}:\s|\s\([\da-zA-Z,\s\-]+\)$","",song.getText())
            anime_op_list.append(song_cleaned)
    for song_list in anime_soup.find_all("div", {"class": "ending"}):
        for song in song_list.find_all("span"):
            song_cleaned = re.sub("^#\d{1,2}:\s|\s\([\da-zA-Z,\s\-]+\)$","",song.getText())
            anime_ed_list.append(song_cleaned)
    # append to db
    db = db.append(pd.Series([anime_title,
                              anime_link,
                              ", ".join(anime_op_list),
                              ", ".join(anime_ed_list)],
                             index=db.columns), ignore_index=True)




# - - - Save file - - -
web.close_current_tab()
db.to_csv('I_am_a_file_a_csv_file_tho.csv', index=False)