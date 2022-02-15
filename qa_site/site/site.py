from selenium import webdriver
#imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.kavinskytech.com/")

print(driver.current_url) 


sleep(3)
inicio = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='index.html' and text()='Início']"))).click()
sleep(3)
sobre = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='sobre.html' and text()='Sobre']"))).click()
sleep(3)
serviços = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='serviços.html' and text()='Serviços']"))).click()
sleep(3)
pesquisar = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Pesquisar']")))
pesquisar.send_keys("abc123")
sleep(3)
fb_icon = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.facebook.com/kavinsky.tech']"))).click()
sleep(4)
driver.execute_script("window.history.go(-1)")
sleep(3)
tw_icon = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://mobile.twitter.com/KavinskyTech']"))).click()
sleep(4)
driver.execute_script("window.history.go(-1)")
sleep(3)
lk_icon = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.linkedin.com/company/kavinsky-tech']"))).click()
sleep(4)
driver.execute_script("window.history.go(-1)")
sleep(3)
ig_icon = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.instagram.com/kavinsky.tech/']"))).click()
sleep(4)
driver.execute_script("window.history.go(-1)") 
sleep(3)
wpp_icon = driver.find_element_by_id("wpp").click()
sleep(4)
driver.execute_script("window.history.go(-1)")
sleep(3)


driver.close()