from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import csvrw


def read(domain):
    driver = webdriver.Chrome()
    data_set = csvrw.readcsv()
    driver.get(domain)

    for keys in data_set:
        driver.get(domain)
        username = driver.find_element(By.ID, 'email')
        password = driver.find_element(By.ID, 'pass')
        login = driver.find_element(By.CLASS_NAME, 'btn')
        username.send_keys(keys[0])
        password.send_keys(keys[1])
        # loginbtn
        action = ActionChains(driver)
        action.click(login)
        action.perform()
        driver.implicitly_wait(5)
        time.sleep(2)


def cdm_ui():
    print("+---NSBM QR---+")
    print("---------------")
    print("1.Add Users")
    print("2.check Details")
    print("3.Run")
    print("***************")

    while True:
        ui_input = input("Enter :")

        if ui_input == "1":
            pass
        elif ui_input == "2":
            pass
            break
        elif ui_input == "3":
            run()
            break
        else:
            print("Value invalied!!!")


#"http://10.10.10.227/login.php?id=20748067200"
def run():
    url = input("Input url: ")
    while True:
        on = input("Do you want to start[Y]:")
        if on.lower() == 'y':
            read(url)
            break


if __name__ == "__main__":
    cdm_ui()





