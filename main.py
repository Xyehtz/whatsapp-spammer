import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

# Funcion para spamear mensajes a un contacto en especifico
# La funcion inicia abriendo el webdriver de Google Chrome, para posteriormente abrir WhatsApp y maximizar la ventana, despues de esto el usuario tiene que iniciar sesion en WhatsApp usando el codigo, posterior a esto tiene que presionar enter en la consola para empezar con el spameo
# El usuario tiene que especificar el nombre o numero de telefono de la persona a espamear en la console, despues de esto el programa se encargara de enviar todo el mensaje 

def spam(path):
    driver = webdriver.Chrome(keep_alive=True)
    driver.get('https://web.whatsapp.com/')
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    driver.maximize_window()

    input("Press enter to confirm that you have entered WhatsApp")

    name = input("Enter the name of phone number of the person to Spam: ")

    user = driver.find_element(By.XPATH, "//span[@title='{}']".format(name))
    user.click()

    time.sleep(5)

    with open(path, 'r') as file:
        for line in file:
            line = line.replace('\n', '').strip()

            if line == '':
                continue

            msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

            print(line)
            msg_box.send_keys(line)
            #time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()

            time.sleep(0.5)

if __name__ == '__main__':
    spam('script.txt')
