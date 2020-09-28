
def Browser_get_soup(link_base):
    import webbot, time
    from bs4 import BeautifulSoup
    web = webbot.Browser()
    web.go_to(link_base)
    time.sleep(3)
    content = web.get_page_source()  # Saca la código fuente de la página
    soup = BeautifulSoup(content, 'html.parser')  # Acá le defino a soup que lo que estoy viendo es un HTML
    return soup