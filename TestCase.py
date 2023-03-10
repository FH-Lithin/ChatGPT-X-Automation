from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://myt-sit.fhcdn.dev")

wait = WebDriverWait(driver, 10)

login = wait.until(EC.presence_of_element_located((By.ID, "login")))
login.send_keys("7033443434")

continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
continue_button.click()