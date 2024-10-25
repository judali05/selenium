from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def actualizar_pantalla(wait, serial, failed_serials):
    try:
        #computadores
        element_primar = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/ul/li[1]/a'))).click()

        #nombre
        element_name = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[1]/div/input')))
        element_name.clear()
        element_name.send_keys("EVERS ANGULO")

        #estado
        element_opcion_1 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[2]/div/div/span/span[1]/span/span[1]'))).click()
        element_opcion_1 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input'))).send_keys("DISPONIBLE")
        element_opcion_1 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[2]/ul/li/ul/li'))).click()

        #localizacion
        element_opcion_2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[3]/div/div/span/span[1]/span/span[1]'))).click()
        element_opcion_2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input'))).send_keys("carvajal > sotano > bodega")
        element_opcion_2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[2]/ul/li/ul/li'))).click()

        #numero de contacto
        element_contacto = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[9]/div/input')))
        element_contacto.clear()

        #nombre de usuario
        element_usuario = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[11]/div/input')))
        element_usuario.clear()
    except Exception as e:
        print(f"Error occurred while updating {serial}: {e}")
        failed_serials.append(serial)  
