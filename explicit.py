from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
	browser = webdriver.Chrome()

	browser.get("http://suninjuly.github.io/wait2.html")

	# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельнjй
	button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.LINK_TEXT, "$100"))
	)

	button.click()
	message = browser.find_element_by_id("verify_message")

	assert "successful" in message.text

finally:
	#ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()