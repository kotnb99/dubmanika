from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link ="https://rozetka.com.ua/"
browzer = webdriver.Chrome()
browzer.maximize_window()
browzer.get(link)

search_string = browzer.find_element(By.CSS_SELECTOR,"input[class*=search-form__input]")
search_string.send_keys("Меблі")
cnopka = browzer.find_element(By.CSS_SELECTOR,"button[class*=button_color_green]")
cnopka.click()
time.sleep(2)
proverka_meb=WebDriverWait(browzer,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h1[class*=ng-star-inserted]"))).text
print(proverka_meb)
proverka="Меблі"
if proverka_meb==proverka:
    print("Хеллоу Ворд")
else:print("Хуита")