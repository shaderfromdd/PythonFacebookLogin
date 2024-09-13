# # import string
# # import random
# # def pwd_generator(size=32, chars=string.ascii_uppercase + string.ascii_lowercase + "!$%&=()%" + string.digits):
# #     print(''.join(random.SystemRandom().choice(chars) for _ in range(size)))
# # pwd_generator()
# import urllib.request
# urllib.request.urlretrieve("https://www.gmx.net", "gmx.html")


from selenium import webdriver
from time import sleep
#v.from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
usr=input('Enter Email Id:') 
pwd=input('Enter Password:') 
 
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)
 
username_box = driver.find_element(By.ID, 'email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
 
password_box = driver.find_element(By.ID, 'pass')
password_box.send_keys(pwd)
print ("Password entered")



# allow_cookies = driver.find_element(By.CSS_SELECTOR, "[aria-label='Allow all cookies']")
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Allow all cookies']//span[text()='Allow all cookies']"))).click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Allow all cookies']"))).click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[text()[contains(., 'Allow all cookies')]]"))).click()
# driver.find_element_by_xpath("//span[contains(text(),'Allow all cookies')]").click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft']"))).click()
#allow_cookies = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft']")))
allow_cookies = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Allow all cookies']")))
#allow_cookies = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Allow all cookies')]")))
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft']"))).click()
allow_cookies.click()
#
#[contains(text(),'someUniqueString')]
# allow_cookies.click()
 
login_box = driver.find_element(By.NAME, 'login')
login_box.click()
 
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
