import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


"""seteamos el webdriver"""
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 

website = 'https://bertoldi.com.ar'
driver.maximize_window()
time.sleep(2)
driver.get(website)

#ACA PROBAMOS EL DESPLEGABLE DE PRODUCTOS
ele= driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div")
#Creating object of an Actions class
a = ActionChains(driver)
#Performing the mouse hover action on the target element.
a.move_to_element(ele).perform()
time.sleep(4)


#ACA COMENZAMOS A PROBAR TODOS LOS LINKS, LOS LINK 5 Y 6 SI LOS DEJAMOS SIN COMENTAR, EL SCRIPT NO FUNCIONA 
link1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[1]/a/span")
link1.click()
time.sleep(2)

link2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]/a/span")
#link2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]/a")
link2.click()
time.sleep(2)

#driver.get(website)

link3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[3]/a/span")
link3.click()
time.sleep(2)

#driver.get(website)

link4 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[4]/a/span")
link4.click()
time.sleep(2)

#driver.get(website)

#link5 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[5]/a/span")
#link5.click()
#time.sleep(2)

#driver.get(website)

#link6 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[6]/a/span")
#link6.click()
#time.sleep(2)

#driver.get(website)

#linkfb = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/a")
#linkfb.click()
#time.sleep(2)

