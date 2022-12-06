# Задание 1
# Откройте http://practice.automationtesting.in/
# Нажмите на вкладку "My Account Menu"
# В разделе "Register", введите email для регистрации
# В разделе "Register", введите пароль для регистрации
# составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# почту и пароль сохраните, потребуюутся в дальнейшем
# Нажмите на кнопку "Register"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
# В разделе "Register", введите email для регистрации
email = driver.find_element_by_id("reg_email")
email.send_keys("leltatina@gmail.com")
# В разделе "Register", введите пароль для регистрации
password = driver.find_element_by_id("reg_password")
password.send_keys("LelTatina969777")
# Нажмите на кнопку "Register"
register = driver.find_element_by_name("register")
register.click()
driver.quit()


#Задание 2
# Откройте http://practice.automationtesting.in/
# Нажмите на вкладку "My Account Menu"
# В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# Нажмите на кнопку "Login"
# Добавьте проверку, что на странице есть элемент "Logout"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
# В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
username = driver.find_element_by_id("username")
username.send_keys("leltatina@gmail.com")
# В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
password2 = driver.find_element_by_id("password")
password2.send_keys("LelTatina969777")
# Нажмите на кнопку "Login"
login = driver.find_element_by_name("login")
login.click()
# Добавьте проверку, что на странице есть элемент "Logout"
logout = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))

driver.quit()