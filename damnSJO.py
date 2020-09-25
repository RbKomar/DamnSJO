from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

url = "https://app.sjo.pw.edu.pl/zapisy/default/index"
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
cnt = 0

# WPISZ TUTAJ SWOJE DANE
faculty = 'Elektroniki i Technik Informacyjnych anglojezyczny'
PESEL = '00000000000'
password = 'password'
language = 'chiński'
year = '2'
sem = '4'
# NO I SIUP PĘTELKA AZ SERVERY NIE ZADZIAŁAJĄ

while True:
    if cnt == 0:
        try:
            driver.find_element_by_xpath(
                '//*[@id="vis"]'
            ).click()
            driver.find_element_by_id('username').send_keys(PESEL)
            driver.find_element_by_id('password').send_keys(password)
            driver.find_elements_by_xpath('// *[ @ id = "fm1"] / div[5] / input[4]')[0].click()
            cnt += 1
        except:
            pass

    try:
        select = Select(driver.find_element_by_id('wyborwydzialuform-wydzial'))
        select.select_by_visible_text(faculty)
        driver.find_elements_by_xpath('/html/body/div/div/div/form/div[2]/div/button')[0].click()
    except:
        pass

    try:
        time.sleep(1)
        driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/a')[0].click()
        driver.find_element_by_id('dj-zapisy').click()
        select = Select(driver.find_element_by_id('zapisyform-jezyk'))
        select.select_by_visible_text(language)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[2]/div/button').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('wybierz').click()
        time.sleep(1)
        select = Select(driver.find_element_by_id('zapisyform-rokstudiow'))
        select.select_by_visible_text(year)
        select = Select(driver.find_element_by_id('zapisyform-semestrstudiow'))
        select.select_by_visible_text(sem)
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div[3]/div/button').click()
        break
    except Exception as e:
        print("Podałeś niepoprawne warunki albo sjo stronka nie działa: \n", e)

    time.sleep(10)
    driver.refresh()

time.sleep(5)
driver.quit()