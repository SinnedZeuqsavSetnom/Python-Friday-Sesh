# # # Objetivos:
# # # Obtener data de MyAnimeList sobre anime de este año
# - - - - - - - - - - Imports - - - - - - - - - -
import re, time
import datetime as dt
import pandas as pd
from bs4 import BeautifulSoup
from webbot import Browser

#tao se la come doblada
# - - - - - - - - - - Set-up - - - - - - - - - -
time_start = time.time()
time_load_search = 3
time_load_article = 2
date_today = dt.date.today()
# data frame & browser
db = pd.DataFrame(columns=["anime",
                           "col1",
                           "col2",
                           "col3"])
link_base = 'https://myanimelist.net/'


# - - - - - - - - - - Webbot Navigation - - - - - - - - - -
web = Browser()
web.go_to(link_base)
time.sleep(time_load_search)
content = web.get_page_source()
soup = BeautifulSoup(content, 'html.parser')

ranking_lists = soup.find_all("li", {"class": "ranking-unit"})
print(ranking_lists[0])
