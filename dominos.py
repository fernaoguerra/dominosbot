import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

def order_pizza():
    options = Options()
    options.add_argument("--disable-popup-blocking")
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    #browser = webdriver.Chrome(chromedriver)
    browser.get('https://www.dominos.com.br/pages/customer/#!/customer/login/')
    #click login
    # browser.find_element_by_xpath('/html/body/header/nav[1]/div[1]/div[3]/span/a').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="Email"]').send_keys('sua senha aqui')
    browser.find_element_by_xpath('//*[@id="Password"]').send_keys('seu password aqui')
    browser.find_element_by_xpath('//*[@id="customerLoginPage"]/div/div/div[2]/div/form/div[15]/div[1]/button/span').click()
    time.sleep(3)

    browser.get("https://www.dominos.com.br/pages/order/#!/locations/search/")

    time.sleep(3)
    print('teste')
    browser.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[1]/label[1]/span[1]').click()
    browser.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[3]/button').click()
    time.sleep(3)
    try:
        browser.find_element_by_xpath('//*[@id="pageModal"]/div/section/div/div/div/button').click()
    except:
        print("no popup")
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="pageModal"]/div/section/div/div/div/button').click()

    #select Meat and Bacon pizza
    time.sleep(2)
    browser.get('https://www.dominos.com.br/pages/order/#!/section/Food/category/Pizza/')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="categoryPage2"]/section[3]/div/div[8]/div/a[1]').click() 

    #go to cart
    time.sleep(1)
    browser.get("https://www.dominos.com.br/pages/order/#!/checkout/")
    try:
        print("entrou no try")
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="genericOverlay"]/section/header/button').click()
        print("printou aqui?")
        time.sleep(3)
        print('sleep 3')
        browser.find_element_by_xpath('//*[@id="js-checkoutColumns"]/aside/div[3]/div[1]/a').click()
        print(" saiu try")
    except:
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="js-checkoutColumns"]/aside/div[3]/div[1]/a').click()

    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="orderPaymentPage"]/form/div[4]/div[1]/div[2]/div/div[5]/label/input').click()
    select = Select(browser.find_element_by_xpath('//*[@id="orderPaymentPage"]/form/div[4]/div[1]/div[2]/div/div[5]/div[2]/div/div/select'))
    select.select_by_value('MasterCard')

    # Fazer pedido
    # browser.find_element_by_xpath('//*[@id="orderPaymentPage"]/form/div[5]/div/div/div[4]/button').click()
