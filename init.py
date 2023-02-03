#post tweet using selenium
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import requests as request
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
senha = os.getenv("SENHA")
usuario = os.getenv("USUARIO")


r = request.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/455/indaiatuba-sp")
temp_maxima = r.text.find("Temperatura máxima")
temp_minima = r.text.find("Temperatura mínima")


temp_maxima = r.text[temp_maxima+108:temp_maxima+110]
temp_minima = r.text[temp_minima+95:temp_minima+97]

now = datetime.datetime.now()
current_date = now.strftime("%d/%m/%Y")

text = 'Na Cidade de Indaiatuba, dia: ' + current_date + ', a temperatura máxima é de ' + temp_maxima + '°C e a mínima é de ' + temp_minima + '°C'


print('Carregando o driver do Chrome...')
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(options=options)
print('Driver carregado com sucesso!')

print('Acessando o Twitter...')
driver.get("https://twitter.com/login")
time.sleep(5)


us_element = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
username = driver.find_element(By.XPATH, us_element)
username.send_keys(email)
time.sleep(0.5)

print('Email digitado com sucesso!')

username.send_keys(Keys.RETURN)
time.sleep(3)

us_element = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
username2 = driver.find_element(By.XPATH, us_element)
if(username2):
    print('Necessário informar usuário')
    username2.send_keys(usuario)
    username2.send_keys(Keys.RETURN)
    time.sleep(2.5)
    print('Usuário digitado com sucesso!')

pass_element = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
password = driver.find_element(By.XPATH, pass_element)
password.send_keys(senha)
password.send_keys(Keys.RETURN)
print('Senha digitada com sucesso!')
time.sleep(3)


auth_token = driver.get_cookie("auth_token")["value"]
ct0 = driver.get_cookie("ct0")["value"]


print('Clica no botão Tweet')
button_tweet_element = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
tweet_button = driver.find_element(By.XPATH, button_tweet_element)
tweet_button.click()
time.sleep(2)

print('Escrevendo o tweet')
box_element = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span/br'
box = driver.find_element(By.XPATH, box_element)
box.send_keys(text)
time.sleep(2)


button_send_element = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div'
button_send = driver.find_element(By.XPATH, button_send_element)
button_send.click()
time.sleep(4)
print('Tweet enviado com sucesso!')

driver.close()