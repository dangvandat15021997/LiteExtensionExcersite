import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def login_with_request(email, password):
    ses = requests.Session()
    payload = {
        'log': email,
        'pwd' : password
    }
    res = ses.post('http://45.79.43.178/source_carts/wordpress/wp-login.php', data = payload)
    
    html_doc = res.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    user_name = soup.find_all('span', {'class': "display-name"})[0].string

  
    return user_name

def login_with_selenium(email, password):
    URL = 'http://45.79.43.178/source_carts/wordpress/wp-admin'
    PATH_DRIVER = './chromedriver_linux64/chromedriver'
    driver = webdriver.Chrome(PATH_DRIVER)

    driver.get(URL)
    search = driver.find_element_by_id('user_login')
    search.send_keys(email)
    search = driver.find_element_by_id('user_pass')
    search.send_keys(password)
    search.send_keys(Keys.RETURN)

    user_name = driver.find_element_by_class_name('display-name').text

    driver.quit()
    
    return user_name


if __name__ == '__main__':
    email = 'admin'
    password = '123456aA'
    user_name1 = login_with_request(email, password)
    print(user_name1)
    user_name2 = login_with_selenium(email, password)
    print(user_name2)