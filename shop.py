# Задание 4
# Откройте http://practice.automationtesting.in/
# Залогиньтесь
# Нажмите на вкладку "Shop"
# Откройте книгу "HTML 5 Forms"
# Добавьте тест, что заголовок книги назвается: "HTML5 Forms"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Залогиньтесь
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("leltatina@gmail.com")
password2 = driver.find_element_by_id("password")
password2.send_keys("LelTatina969777")
login = driver.find_element_by_name("login")
login.click()
# Нажмите на вкладку "Shop"
shop = driver.find_element_by_id("menu-item-40")
shop.click()
# Откройте книгу "HTML 5 Forms"
book = driver.find_element_by_css_selector(".post-181 h3")
book.click()
#Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
element = driver.find_element_by_css_selector(".product_title.entry-title")
element_get_text = element.text
assert element_get_text == "HTML5 Forms"
driver.quit()

#  Задание 5
#  Откройте http://practice.automationtesting.in/
#  Залогиньтесь
#  Нажмите на вкладку "Shop"
#  Откройте категорию "HTML"
#  Добавьте тест, что отображается три товара

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#  Залогиньтесь
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("leltatina@gmail.com")
password2 = driver.find_element_by_id("password")
password2.send_keys("LelTatina969777")
login = driver.find_element_by_name("login")
login.click()
#  Нажмите на вкладку "Shop"
shop = driver.find_element_by_id("menu-item-40")
shop.click()
#  Откройте категорию "HTML"
html = driver.find_element_by_link_text("HTML")
html.click()
#  Добавьте тест, что отображается три товара
product = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
assert len(product) == 3
driver.quit()

#  Задание 6
#  Откройте http://practice.automationtesting.in/
#  Залогиньтесь
#  Нажмите на вкладку "Shop"
#  Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
#  Используйте проверку по value
#  Отсортируйте товары по цене от большей к меньшей
#  в селекторах используйте класс Select
#  Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
#  Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
#  Используйте проверку по value

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#  Залогиньтесь
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("leltatina@gmail.com")
password2 = driver.find_element_by_id("password")
password2.send_keys("LelTatina969777")
login = driver.find_element_by_name("login")
login.click()
#  Нажмите на вкладку "Shop"
shop = driver.find_element_by_id("menu-item-40")
shop.click()
#  Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
from selenium.webdriver.support.select import Select
status_selector = driver.find_element_by_css_selector(".woocommerce-ordering .orderby")
status_selector_def = status_selector.get_attribute("value")
if status_selector_def == "menu_order":
    print("Выбрано значение Default sorting")
else:
    print("Выбрано другое значение")
#  Отсортируйте товары по цене от большей к меньшей, в селекторах используйте класс Select
element = driver.find_element_by_name("orderby")
select = Select(element)
select.select_by_value("price-desc")
#  Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
status_selector = driver.find_element_by_css_selector(".woocommerce-ordering .orderby")
#  Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей, используйте проверку по value
status_selector_sort = status_selector.get_attribute("value")
if status_selector_sort == "price-desc":
    print("Выбрана сортировка Sort by price: high to lowg")
else:
    print("Сортировка Sort by price: high to low не выбрана")
driver.quit()

# Задание 7
# Откройте http://practice.automationtesting.in/
# Залогиньтесь
# Нажмите на вкладку "Shop"
# Откройте книгу "Android Quick Start Guide"
# Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# Добавьте явное ожидание и нажмите на обложку книги
# Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
# Залогиньтесь
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("leltatina@gmail.com")
password2 = driver.find_element_by_id("password")
password2.send_keys("LelTatina969777")
login = driver.find_element_by_name("login")
login.click()
# Нажмите на вкладку "Shop"
shop = driver.find_element_by_id("menu-item-40")
shop.click()
# Откройте книгу "Android Quick Start Guide"
android_guide = driver.find_element_by_css_selector(".post-169 h3")
android_guide.click()
# Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
old_price = driver.find_element_by_css_selector(".price > del > span")
new_price = driver.find_element_by_css_selector(".price > ins > span")
old_price_text = old_price.text
new_price_text = new_price.text
assert old_price_text == "₹600.00"
assert new_price_text == "₹450.00"
# Добавьте явное ожидание и нажмите на обложку книги
book = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
book.click()
# Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
close.click()
driver.quit()


# Задание 9
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Нажмите на вкладку "Shop"
shop = driver.find_element_by_id("menu-item-40")
shop.click()
# Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
webapp = driver.find_element_by_css_selector(".post-182 .button")
webapp.click()
time.sleep(5)
algorithm = driver.find_element_by_css_selector(".post-180 .ajax_add_to_cart")
algorithm.click()
# Перейдите в корзину
basket = driver.find_element_by_class_name("cartcontents")
basket.click()
# Удалите первую книгу. Перед удалением добавьте sleep
time.sleep(5)
delete = driver.find_element_by_css_selector("a[data-product_id='180']")
delete.click()
# Нажмите на Undo (отмена удаления)
undo = driver.find_element_by_link_text("Undo?")
undo.click()
# В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“.
# Предварительно очистите поле с помощью локатор_поля.clear()
element = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
element.clear()
element.send_keys("3")
# Нажмите на кнопку "UPDATE BASKET"
update = driver.find_element_by_name("update_cart")
update.click()
# Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
value = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
value_1 = value.get_attribute("value")
assert value_1 == "3"
#  Нажмите на кнопку "APPLY COUPON". Перед нажатимем добавьте sleep
time.sleep(5)
apply = driver.find_element_by_name("apply_coupon")
apply.click()
#  Добавьте тест, что возникло сообщение: "Please enter a coupon code."
text = driver.find_element_by_class_name("woocommerce-error")
text_text = text.text
assert text_text == "Please enter a coupon code."
driver.quit()

