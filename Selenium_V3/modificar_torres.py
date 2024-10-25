from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def actualizar_torre(wait, serial, failed_serials):
        try:
                #computadores
                element_primar = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/ul/li[1]/a'))).click()
                
                #bodega
                element_opcion_4 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[2]/div/div/div/div/div/div/div[3]/div/div/span[1]/span[1]/span/span[1]'))).click()
                element_input_4 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field'))).send_keys("espacio armarios")
                element_opcion_4 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[2]/ul/li/ul/li/span'))).click()
                
                #nombre
                element_name = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[1]/div/input')))
                element_name.clear()
                element_name.send_keys("JESUS DAVID VANEGAS")

                #estado
                element_opcion_1 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[2]/div/div/span/span[1]/span/span[1]'))).click()
                element_opcion_1 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input'))).send_keys("A cargo de")
                element_opcion_1 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[2]/ul/li/ul/li'))).click()

                #localizacion
                element_opcion_2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[3]/div/div/span/span[1]/span/span[1]'))).click()
                element_opcion_2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input'))).send_keys("carvajal > sotano > Timac")
                element_opcion_2 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[2]/ul/li/ul/li'))).click()

                #numero de contacto
                element_contacto = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[9]/div/input')))
                element_contacto.clear()

                #nombre de usuario
                element_usuario = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[11]/div/input')))
                element_usuario.clear()

                # comentarios
                element_comentario = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[17]/div/textarea')))
                element_comentario.clear()
                element_comentario.send_keys('Borrado seguro de ENEL')

                #fuente de actualizacion
                element_opcion = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/div/div[18]/div/div/span[1]/span[1]/span/span[1]'))).click()
                element_opcion = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input'))).send_keys("bodega carvajal")
                element_opcion = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/span/span/span[2]/ul/li/span/span'))).click()

                #botton  
                element_button = wait.until(EC.element_to_be_clickable((By.NAME, 'update'))).click()

        except Exception as e:
                print(f"Error occurred while updating {serial}: {e}")
                failed_serials.append(serial)  


