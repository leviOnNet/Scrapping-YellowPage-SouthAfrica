from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import os
import path
import json
import pandas as pd


options =Options()
options.headless = False
options.add_argument("--window-size=1400,1000")

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
get_url = 'https://www.yellowpages.co.za/search?what=restaurants&where=hatfield&'

def main_request(get_url,x):
    r           = driver.get(get_url + f'pg={x}')
    return r




for x in range(1,3):
    print(x)
    main_request(get_url,x)
    resturant_names = driver.find_elements_by_class_name('nameOverflow')
    names_array= []
    first_number = driver.find_elements_by_class_name('fullDetailId')
    main_number = []
  
   
    

    for i in range(len(resturant_names)):
        names_array.append(resturant_names[i].text)
        
        main_number.append(first_number[i].text)
        
        

print(names_array)
print(main_number)



