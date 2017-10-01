from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

browser = webdriver.Firefox()
browser.get("https://panda.ime.usp.br/pensepy/static/pensepy/10-Arquivos/files.html")
time.sleep(10)