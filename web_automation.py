from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

my_options = Options()
# my_options.add_argument("--headless")
# my_options.add_argument("--window-size=1920,1080")
my_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=my_options)

driver.get("https://www.google.com/")

# Find the searchbox
search_box = driver.find_element(By.NAME, "q")

time.sleep(2)

# Enter search keyword
search_box.send_keys("Hello")

time.sleep(2)

# Hit the Enter(Return) key
search_box.send_keys(Keys.RETURN)

time.sleep(10)

driver.quit()