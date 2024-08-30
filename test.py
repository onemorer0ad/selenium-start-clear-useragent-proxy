from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

from config import login, password, proxy_login, proxy_password

options = Options()
options.add_argument(f"user-agent={UserAgent().random}")
# отключаем webdriver-mode
options.add_argument("--disable-blink-features=AutomationControlled")


# proxy autorization
proxy_options = {
    'proxy': {
        'http': f'http://{proxy_login}:{proxy_password}@188.130.210.72:3000',
        'https': f'http://{proxy_login}:{proxy_password}@188.130.210.72:3000'
    }
}

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                          options=options,
                          seleniumwire_options= proxy_options
                          )


url = 'https://www.2ip.ru/'
driver.get(url)

# Нажимаем на sign, вводим логин и пароль, кликаем на логин
# driver.implicitly_wait(5)
# driver.find_element(by = By.XPATH, value='/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a').click()
# driver.implicitly_wait(5)
# driver.find_element(By.ID, 'login_field').send_keys(login)
# driver.implicitly_wait(5)
# driver.find_element(By.ID, 'password').send_keys(password)
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]').click()
time.sleep(30)