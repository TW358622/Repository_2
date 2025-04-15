from selenium import webdriver
from selenium.webdriver.common.by import By # use in locators
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

path = "https://www.google.com"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(path)

driver.find_element(By.CLASS_NAME, 'gb_X').click()
sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[5]/a[2]').click()
# sleep(1)
# gmail = driver.find_element(By.ID, 'identifierId')
# gmail.send_keys('kiruhs@gmail.com')
# sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/header/div/div[5]/gws-dropdown-button/div').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/header/div/div[5]/gws-dropdown-button/a[1]/span').click()
sleep(1)
first = driver.find_element(By.ID,'firstName')
first.click()
first.send_keys('Alexander')
driver.find_element(By.ID,'collectNameNext').click()
try:
    if driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[2]/div[2]/span'):
        print("The test is failed")
except:
        print("The test is passed")
# Next 6 rows are related to negative test when there is no Firstname entered
# driver.find_element(By.ID,'collectNameNext').click()
# try:
#     if driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[2]/div[2]/span'):
#         print("The test is passed")
# except:
#         print("The test is failed")
sleep(5)
month = Select(driver.find_element(By.ID, 'month'))
month.select_by_value('11')

day = driver.find_element(By.ID,'day')
day.send_keys('0')

year = driver.find_element(By.ID,'year')
year.send_keys('1000')

gender = Select(driver.find_element(By.ID,'gender'))
gender.select_by_visible_text('Male')
sleep(5)
nxt = driver.find_element(By.ID,'birthdaygenderNext')
nxt.click()
sleep(5)
try:
    if driver.find_element(By.XPATH, '//*[@id="dateError"]/div/text()'):
        print('The test is failed')
except:
    print("The test is passed")

day = driver.find_element(By.ID,'day')
day.send_keys(Keys.CONTROL + 'a')
day.send_keys('30')

year = driver.find_element(By.ID,'year')
year.send_keys(Keys.CONTROL + 'a')
year.send_keys('1971')

nxt.click()

sleep(5)
driver.quit()