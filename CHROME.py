import time
from selenium import webdriver
# no GUI
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# local desktop
browser = webdriver.Chrome(options=options)
url = 'https://www.eeagd.edu.cn/healthcodewx/?nickname=Unknown&headimgurl=http://thirdwx.qlogo.cn/mmopen/vi_32/pibZQS4ZOCh8tURp4YlGDPzvMOMe9ID8SNN6fgHBIicv3Cz8cnF8iaxSQnVCZu0Ue2fvTl42cKAUHmNp0yf1BU5eA/132&from=groupmessage#/login'
browser.get(url)
print("Got into the Website")
# username & password
browser.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input').send_keys({Username})
browser.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/input').send_keys({Password})
print("Sent keys OK")
# login
browser.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/button').click()
time.sleep(2)
print("Login successfully")
# health check in
browser.find_element_by_xpath('html/body/div[1]/div[1]/div[3]/button').click()
time.sleep(2)
# accept
browser.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]').click()
# submit
browser.find_element_by_xpath('html/body/div[1]/div[1]/div[1]/div[1]/button').click()
print("Submitted")

