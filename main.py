import os
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()
username = os.getenv('username')
password = os.getenv('password')
file_path = os.path.abspath('image1.jpg')

browser = webdriver.Firefox()

browser.get("https://www.instagram.com/")
browser.implicitly_wait(5)
username_input = browser.find_element(By.NAME, 'username')
password_input = browser.find_element(By.NAME, 'password')
login_link = browser.find_element(By.TAG_NAME, "button")
username_input.send_keys(username)
password_input.send_keys(password)
login_link.click()

browser.implicitly_wait(5)
create_link = browser.find_element(By.XPATH, "//span[text()='Create']")
create_link.click()
browser.implicitly_wait(5)
file_input = browser.find_element(By.XPATH, "//input[@type='file']")
browser.implicitly_wait(5)
file_input.send_keys(file_path)
browser.implicitly_wait(5)
next_link = browser.find_element(By.XPATH, "//div[text()='Next']")
browser.implicitly_wait(5)
next_link.click()
browser.implicitly_wait(5)
next_link2 = browser.find_element(By.XPATH, "//div[text()='Next']")
browser.implicitly_wait(5)
next_link2.click()
browser.implicitly_wait(5)
caption_link = browser.find_element(By.XPATH, "//div[@aria-label='Write a caption...']")
# p_tag = browser.
message = '<p class="xdj266r x11i5rnm xat24cr x1mh8g0r" dir="ltr"><span data-lexical-text="true">fsadfsa</span><br><br><span data-lexical-text="true">fasdfsa</span></p>'
caption_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Write a caption...']"))
)
caption_input.send_keys("Sizning xabaringiz")
# caption_link.send_keys(message)
# caption_link.send_keys('ofsda')
# p_tag = caption_link.execute_script("return document.getElementById('hidden_element_id');")
# p_tag = caption_link.find_element(By.TAG_NAME, 'p')
# print(p_tag.text)
# browser.execute_script("arguments[0].innerText = arguments[1];", p_tag, message)
# print(p_tag.text)
# print(caption_link.text)
# p_tag.send_keys("hello world")
# share_link = browser.find_element(By.XPATH, "//div[text()='Share']")
# share_link.click()
# try:
#     success = WebDriverWait(driver=browser, timeout=60).until(
#         EC.visibility_of_element_located((By.XPATH, "//div[text()='Post shared']"))
#     )
#     print("Uploaded succesully")
#     browser.quit()
# except Exception as e:
#     print("Failed", e)
#     browser.quit()


