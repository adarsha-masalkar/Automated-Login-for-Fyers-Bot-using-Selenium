from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")

    client_id = 'Client Id'
    password = 'yourpassword'
    pin = '1234'

    redirect_uri = 'https://old-login.fyers.in/'

    service = Service("Path to Chrome Webdriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(redirect_uri)
    driver.maximize_window()
    time.sleep(2)

    login_id = driver.find_element(By.ID, 'fy_client_id')
    login_id.send_keys(client_id)
    submit_button_1 = driver.find_element(By.ID, 'clientIdSubmit')
    submit_button_1.click()
    time.sleep(1)

    client_password = driver.find_element(By.ID, 'fy_client_pwd')
    client_password.send_keys(password)
    submit_button_2 = driver.find_element(By.ID, 'loginSubmit')
    submit_button_2.click()
    time.sleep(1)

    client_pin_first_list = driver.find_elements(By.ID, 'first')
    client_pin_first = client_pin_first_list[1]
    client_pin_first.send_keys(pin[0])
    client_pin_second_list = driver.find_elements(By.ID, 'second')
    client_pin_second = client_pin_second_list[1]
    client_pin_second.send_keys(pin[1])
    client_pin_third_list = driver.find_elements(By.ID, 'third')
    client_pin_third = client_pin_third_list[1]
    client_pin_third.send_keys([2])
    client_pin_fourth_list = driver.find_elements(By.ID, 'fourth')
    client_pin_fourth = client_pin_fourth_list[1]
    client_pin_fourth.send_keys(pin[3])
    time.sleep(1)
    submit_button_3 = driver.find_element(By.ID, 'verifyPinSubmit')
    submit_button_3.click()
    time.sleep(1)

    return True


if __name__ == '__main__':
    main()
