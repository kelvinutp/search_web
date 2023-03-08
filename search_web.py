#monitors specific website for changes in URLs

import os
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

def get_urls(class_='', id=''):
    '''

    extracts all the links present on currently active website\n
    returns two (2) list type object
    class_= class within HTML (optional)
    id= id within HTML (optional)
    '''
    time.sleep(5)
    links=[]
    incomp_links=[]
    print('getting urls')
    for z in range(2):#el for es por si acaso hay que hacer scroll down
        estado_actual=BeautifulSoup(driver.page_source,'html.parser')
        contenido=estado_actual.find_all(class_=class_)[0]
        for a in contenido.find_all('a'):
            if a.get('href')!=None and 'http' in a.get('href'):
                if a.get('href') not in links:
                    links.append(a.get('href'))
            else:
                if a.get('href') not in incomp_links:
                    incomp_links.append(a.get('href')) #incomplete links
        pi.press('end',presses=2)
    return links,incomp_links
    
def save_content(dest='Downloads',name=''):
    '''
    used for saving PDF or images

    dest: destination where file will be saved, default destination is 'Downloads' \n\n
    name: file name. If no name is provided, it will be saved by the name provided by the browser
    '''
    print('guardando PDF/imagen')
    pi.hotkey('ctrl','s',interval=0.5)
    if name!='':
        pi.write(name)
    time.sleep(5)
    pi.hotkey('ctrl','l',interval=1)
    pi.write(dest)
    pi.press('enter')
    time.sleep(5)
    pi.press('enter',presses=3,interval=1)
    return os.path.join(dest,name)


    


if __name__=='__main__':
    date=str(datetime.now())[:10]+'\n'

    r=r'C:\Users\CIDETYS-AIP\Desktop\python'
    #uses microsoft Edge (for windows systems)
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    # url=input('Ingrese url: ')
    # url=r'https://www.instagram.com/cidetysaip/'
    url=r'https://www.senacyt.gob.pa/convocatorias-redireccion/'
    # url=r'https://utp.ac.pa/calendarios'
    #open webpage
    driver.get(url)

    # print(save_content(dest=r, name='calendario'))
    print(get_urls(class_='sidebar-before-loop'))
    time.sleep(10)

    driver.quit()