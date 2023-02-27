#monitors specific website for changes in URLs

import time
import pandas as pd
import PyPDF2 as pdf
import subprocess as sp
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from search_web import save_content
import os
from read_pdf import info

#[:10] yyyy-mm-dd
#[:13] yyyy-mm-dd hh
#[:16] yyyy-mm-dd hh:mm
#[:19] yyyy-mm-dd hh:mm:ss

def fecha():
    driver.get(links[0])
    #downloading PDF
    q=save_content(os.getcwd(),'calendario_admin.pdf')
    print(q)

    #extracting PDF content
    r=info(q)
    s=r['page_1']
    fechasq=s.split('\n')[2] #fechas de pago de quincena
    print('fecha de quincenca')
    for a in fechasq.split():
        print(a)

    fechasd=s.split('\n')[3] #fechas de pago de decimo tercer mes
    print('fecha de decimo tercer mes')
    for a in fechasd.split():
        print(a)

date=str(datetime.now())[:10]+'\n'

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
url=r'https://utp.ac.pa/calendarios'#pagina web que desea monitorear

driver.get(url)

estado_actual=BeautifulSoup(driver.page_source,'html.parser')
contenido=estado_actual.find_all(id='content-area')[0]
links=[]
for a in contenido('a'):
    if a.get('href')!=None and 'utp.ac.pa/' in a.get('href'):
        links.append(a.get('href')+'\n')

#leyendo el archivo 'links.hlml'
url=r'C:\Users\CIDETYS-AIP\Desktop\python\links.html'
with open(url,'r+') as file:
    #fecha de ultima revision 
    a=file.readlines()
    revision=a[1].strip() #last update date
    content=a[2]
    if revision!=date: #compara fechas
        if links[0]!=content: #compara el ultimo link
            b=file.write('Ultima revision:\n')
            file.write(date)
            file.writelines(links)
            msg='msg CIDETYS-AIP /TIME 3 [Hay cambios en el calendario, revisando]'
            sp.check_output(msg.split())
            fecha()
        else:
            msg='msg CIDETYS-AIP /TIME 3 [Sin cambios]'

file.close()

sp.check_output(msg.split())
time.sleep(5)
#si se ha agregado contenido, porque hubo algun cambio
#buscar como extraer la informacion del pdf correspondiente

time.sleep(10)

driver.quit()

