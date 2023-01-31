#monitors specific website for changes in URLs

import time
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pyautogui as pi

#[:10] yyyy-mm-dd
#[:13] yyyy-mm-dd hh
#[:16] yyyy-mm-dd hh:mm
#[:19] yyyy-mm-dd hh:mm:ss


date=str(datetime.now())[:10]+'\n'

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
url=r'https://utp.ac.pa/sites/default/files/documentos/2023/pdf/calendario-1-semestre-2023-web.pdf'#pagina web que desea monitorear

driver.get(url)

pi.hotkey('ctrl','s')
time.sleep(1)
pi.hotkey('ctrl','L')
pi.write('Downloads')
time.sleep(10)
pi.write('calendario')

pi.hotkey('enter')

time.sleep(10)

driver.quit()