# Задание 1
# Откройте http://practice.automationtesting.in/
# Проскролльте страницу вниз на 600 пикселей
# Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# Нажмите на вкладку "REVIEWS"
# Поставьте 5 звёзд
# Заполните поле "Review" сообщением: "Nice book!"
# Заполните поле "Name"
# Заполните "Email"
# Нажмите на кнопку "SUBMIT"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# Нажмите на название книги "Selenium Ruby"
selenium_ruby = driver.find_element_by_css_selector(".text-22-sub_row_1-0-2-0-0 .attachment-shop_catalog")
selenium_ruby.click()
# Нажмите на вкладку "REVIEWS"
reviews = driver.find_element_by_class_name("reviews_tab")
reviews.click()
# Поставьте 5 звёзд
star_5 = driver.find_element_by_class_name("star-5")
star_5.click()
# Заполните поле "Review" сообщением: "Nice book!"
your_review = driver.find_element_by_id("comment")
your_review.send_keys("Nice book!")
# Заполните поле "Name"
name = driver.find_element_by_id("author")
name.send_keys("Olga")
# Заполните "Email"
email = driver.find_element_by_id("email")
email.send_keys("123@gmail.com")
#Нажмите на кнопку "SUBMIT"
submit = driver.find_element_by_id("submit")
submit.click()

driver.quit()