from tqdm.notebook import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd


def get_oil_info(soup):

    os_info ={}

    ## 주유소 이름
    os_name = soup.find_all(class_="header")
    os_info["이름"] = os_info[0].find(id = "os_nm").text

    ## 주유소 상표
    os_property = soup.find_all(id = "poll_div_nm")
    os_info["상표"] = os_property[0].text

    ## 휘발유 가격
    gasoline_price = soup.find_all( id = "infoTbody")
    os_info["휘발유 가격"] = gasoline_price[0].find(id = "b027_p").text

    ## 경유 가격
    disel_price = soup.find_all(id = "infoTbody")
    os_info["경유 가격"] = disel_price[0].find(id = "d047_p").text

    ## 부가 기능
    add_info = soup.find_all(class_ = "service")
    for info in add_info[0].find_all("img"):
        if not "off" in info["src"]:
            os_info["부가기능"] = {info["alt"] : "o" }
        else:
            os_info["부가기능"] = {info["alt"] : "x" }    

    return os_info


def make_df(os_data):
    
    os_df = pd.DataFrame(os_data)
    print(os_df)
    


if __name__ == "__main__":

    options = webdriver.ChromeOptions()

    prefs = {'download.default_directory':'../../data/html/',
            'download.prompt_for_download' : False}
    options.add_experimental_option('prefs', prefs)

    url = "https://www.opinet.co.kr/searRgSelect.do"
    driver = webdriver.Chrome(service=Service("../../driver/chromedriver-linux64/chromedriver"),
                              options=options)
    
    driver.get(url)

    sigungu = driver.find_element(By.ID, "SIGUNGU_NM0")
    sigungu_list = sigungu.find_elements(By.TAG_NAME, "option")

    sigungu_nm_list = []
    for idx, sigungu_name in enumerate(sigungu_list):
        sigungu_nm_list.append(sigungu_name.get_attribute("value"))

    os_data = []
    for sigungu_name in tqdm(sigungu_nm_list):
        sigungu = driver.find_element(By.ID, "SIGUNGU_NM0")
        sigungu.send_keys(sigungu_name)

        gasoline = driver.find_element(By.XPATH, '''//*[@id="os_layer2"]/p/a''')
        gasoline.click()
        oilstation = driver.find_element(By.XPATH, '''//*[@id="body1"]/tr[1]/td[1]/a''')
        oilstation.click()

        

        os_data.append(get_oil_info(soup))
        
        time.sleep(3)

    make_df(os_data)
    driver.close()    


