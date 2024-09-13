from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options 
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


allow_cookies = driver.find_elements(By.CSS_SELECTOR, "[aria-label='Allow all cookies']")
#allow_cookies[0].screenshot("screenshot.png")
#allow_cookies[1].screenshot("screenshot1.png")
driver.execute_script("arguments[0].click();", allow_cookies[1])
sleep(1)



login_box = driver.find_element(By.NAME, 'login')
login_box.click()
 
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")

