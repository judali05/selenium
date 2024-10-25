from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from explorar_sitio import nav
from login_usuario import login
import time
import getpass

def main():
    service = Service(executable_path='Selenium/drivers/chromedriver.exe')
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)



    wait= WebDriverWait(driver, 10)
    failed_serials = []  
    
    try:
        # username = str(input("ingresa tu usuario: "))
        # password = getpass.getpass("ingresa tu contraseña: ")
        seriales = []
        
        print("ingrese el serial o activo [Presione enter sin ingresar nada para continuar]")
        
        while True:
            serial = input("Serial: ").strip()
            if serial:
                seriales.append(serial)
            else:
                break
        
        if seriales:
            login(driver, wait)
            time.sleep(4)
            
            nav(seriales, wait, failed_serials)
            time.sleep(4)
            
        else:
            print("No se han ingresado valores")
    
        if failed_serials:
            print("\nLos siguientes seriales fallaron en el proceso:")
            for failed_serial in failed_serials:
                print(f" - {failed_serial}")
        else:
            print("\nTodas las operaciones se realizaron correctamente.")
            
    except Exception as e:
        print(f"Se produjo un error: {e}")
    
    finally:
        driver.quit()
    
if __name__ == "__main__":
    main()
