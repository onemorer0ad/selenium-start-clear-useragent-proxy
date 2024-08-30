from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool

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



def selenium_start(url):
    try:
        driver.get(url)
        time.sleep(15)
    except Exception as exc:
        print(exc)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes= 3)
    urls = ['https://google.com', 'https://2ip.ru', 'https://vk.com']

    p.map(selenium_start, urls)