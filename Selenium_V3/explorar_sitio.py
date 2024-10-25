from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from modificar_torre import actualizar_torre
from modificar_pantalla import actualizar_pantalla

def nav(seriales, wait, failed_serials):
    
    for serial in seriales:
        try:
            search_field = wait.until(EC.presence_of_element_located((By.NAME, 'globalsearch')))
            search_field.clear()
            search_field.send_keys(serial)
            
            search_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/header/div/div[1]/form/div/span/button'))).click()

            try:
                primer_elemento = wait.until(EC.element_to_be_clickable((By.XPATH, '//table/tbody/tr[1]/td[1]/a'))).click()
            except Exception as e:
                failed_serials.append(serial)  
                continue  

            actualizar_torre(wait, serial, failed_serials)

            # actualizar_pantalla(wait, serial, failed_serials)

        except Exception as e:
            failed_serials.append(serial)()
