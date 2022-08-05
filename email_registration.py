import os
import random
import unittest
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

load_dotenv()

WEB_SESSION = os.getcwd() + '\\web-session'

REGISTRATION_PAGE = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

driverPath = os.getcwd() + '\\chromedriver.exe'

pswd = os.getenv('pswd')

r1 = random.randint(0,1000)
var = 'tashianna' + str(r1) + '@gmail.com'

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
driver.maximize_window()

def accRegistration() :
    #first email registration
    driver.get(REGISTRATION_PAGE)
    driver.find_element(By.ID,'email_create').send_keys(var)
    driver.find_element(By.ID,'SubmitCreate').click()
    #personal information
    driver.implicitly_wait(20)
    driver.find_element(By.ID, 'id_gender2').click()
    driver.find_element(By.ID,'customer_firstname').send_keys('Tashianna')
    driver.find_element(By.ID,'customer_lastname').send_keys('Putri')
    driver.find_element(By.ID,'passwd').send_keys(pswd)
    #select date
    d = driver.find_element(By.ID,'days')
    d_drp = Select(d)
    d_drp.select_by_index(29)
    #select month
    driver.implicitly_wait(10)
    m = driver.find_element(By.ID,'months')
    m_drp = Select(m)
    m_drp.select_by_index(12)
    #select years
    driver.implicitly_wait(10)
    y = driver.find_element(By.ID,'years')
    y_drp = Select(y)
    y_drp.select_by_index(28)

    #personal address
    driver.implicitly_wait(10)
    driver.find_element(By.ID,'company').send_keys('XYZ Company')
    driver.find_element(By.ID,'address1').send_keys('Address1')
    driver.find_element(By.ID,'city').send_keys('XYZ City')
    #select state
    s = driver.find_element(By.ID,'id_state')
    s_drp = Select(s)
    s_drp.select_by_visible_text('Alabama')
    driver.find_element(By.ID,'postcode').send_keys('12345')
    driver.find_element(By.ID,'phone_mobile').send_keys('021666')

    #submit account
    driver.find_element(By.ID,'submitAccount').click()

    #signout
    driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[2]/a').click()

    #relogin using random acc
    driver.find_element(By.ID,'email').send_keys(var)
    driver.find_element(By.ID,'passwd').send_keys(pswd)
    driver.find_element(By.ID,'SubmitLogin').click()

accRegistration()


