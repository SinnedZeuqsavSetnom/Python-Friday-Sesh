# # # Objetivos:
# # # Obtener data de MyAnimeList sobre anime de este año
# - - - - - - - - - - Imports - - - - - - - - - -
import re, time
import datetime as dt
import pandas as pd
from bs4 import BeautifulSoup
from webbot import Browser


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
web = Browser()
web.go_to(url_pubmed)
time.sleep(time_loadsearch)
content = web.get_page_source()
soup = BeautifulSoup(content, 'html.parser')