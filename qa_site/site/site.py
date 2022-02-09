from selenium import webdriver
#imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()

driver.get("http://site-lb-prd-1761125143.sa-east-1.elb.amazonaws.com/index.html")

print(driver.current_url) 
print(driver.title)
print(driver.desired_capabilities['browserVersion'])

sleep(3)
inicio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='index.html' and text()='Início']"))).click()
sleep(3)
sobre = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='sobre.html' and text()='Sobre']"))).click()
sleep(3)
serviços = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='serviços.html' and text()='Serviços']"))).click()
sleep(3)
contato = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#Contato1.html' and text()='Contato']"))).click()
sleep(3)




driver.close(
