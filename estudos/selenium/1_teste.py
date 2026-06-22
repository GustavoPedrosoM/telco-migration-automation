from selenium import webdriver
import time

# abre o navegador
driver = webdriver.Chrome()

# acessa um site de teste
driver.get("https://google.com")

time.sleep(5)

driver.quit()