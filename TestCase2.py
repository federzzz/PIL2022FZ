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


requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

def compareLabels():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")


#comprarButton = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/button')   
#Aquí identificamos el elemento

labelLinkMarcas = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/nav/ul/li[2]/a/span').text
#Aquí extraemos el texto dentro del elemento



labelObtained = labelLinkMarcas

print(labelObtained)

requirement = 'MARCAS'

compareLabels()

