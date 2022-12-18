import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 

website = 'https://bertoldi.com.ar'
driver.maximize_window()
time.sleep(2)
driver.get(website)

linkface = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/a')

linkface.click()
time.sleep(3)


fb = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/a').get_attribute("href")

if fb == "https://www.facebook.com/bertoldioficial/":
  print("Fuiste redirigido a Facebook exitosamente")
else:
  print("Error")

#print (driver.current_url)
#print (driver.find_element_by_xpath("//div[@class='fb-like-code']/a").get_attribute('href'))




