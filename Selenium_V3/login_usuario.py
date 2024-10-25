from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login(driver, wait):
    driver.get('http://172.27.48.34/index.php?noAUTO=1')
    
    username_file = wait.until(EC.presence_of_element_located((By.ID, 'login_name'))).send_keys("julrojsa")
    password_file = wait.until(EC.presence_of_element_located((By.ID, 'login_password'))).send_keys("Mantecada1")
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, 'submit'))).click()


    
