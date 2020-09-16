from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import time


def scrape_item(item):
    time.sleep(0.5)
    driver.get(item)
    time.sleep(2)
    name = driver.find_element_by_xpath('//span[@class="css-euydo4"]')
    type = driver.find_element_by_xpath('//a[@class="css-lrl8sh "]')
    price = driver.find_element_by_xpath('//div[@class="css-slwsq8 "]/span')
    try:
        ing_btn = driver.find_element_by_xpath('//button[contains(@id, "tab") and .//span[text()="Ingredients"]]')
        driver.execute_script("arguments[0].click();", ing_btn)
        ingredients = driver.find_element_by_xpath('//div[@id="tabpanel2"]/div[@class="css-pz80c5"]')
        ingredients_data = ingredients.text
    except NoSuchElementException:
        ingredients_data = ''
    print(name.text)
    print(type.text)
    print(ingredients_data)
    print(price.text)
    data = [name.text, type.text, ingredients_data, price.text]
    with open('Sun Care.csv', 'a', newline='', encoding="utf-8") as f2:
        writer2 = csv.writer(f2)
        writer2.writerow(data)
    driver.execute_script("window.history.go(-1)")
    time.sleep(1)
    pass


driver = webdriver.Chrome(r'C:\Users\Lenovo\PycharmProjects\PyPrac/chromedriver')
driver.maximize_window()
url = 'https://www.sephora.com/shop/sunscreen-sun-protection'
driver.get(url)

with open('Sun Care.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Type', 'Ingredients', 'Price'])

curr_page_num = 1
is_next = True

while is_next:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.8);")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.2);")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.4);")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.6);")
    time.sleep(0.5)

    items = driver.find_elements_by_xpath('//a[@class="css-ix8km1"]')
    hrefs = [] * 60
    for item in items:
        hrefs.append(item.get_attribute('href'))

    for item in hrefs:
        scrape_item(item)
        time.sleep(0.25)

    try:
        next_page = driver.find_element_by_xpath('//button[@class="css-4ktkov "]')
    except NoSuchElementException:
        is_next = False

    time.sleep(0.5)
    curr_page_num += 1
    url_next = url + '?currentPage=' + str(curr_page_num)
    driver.get(url_next)
    time.sleep(0.5)


time.sleep(1)
driver.close()