from selenium import webdriver
from playsound import playsound
import time
url='https://telegov.njportal.com/njmvc/AppointmentWizard/17'

options=webdriver.ChromeOptions()
options.add_argument('--headless')
driver=webdriver.Chrome(options=options)
driver.get(url)

locations_i_can_go=set(['North BergenPermits','NewarkPermits','LodiPermits','PatersonPermits','BayonnePermits'])

def get_it_done(driver):
    while True:
        driver.refresh()
        divs=driver.find_elements_by_class_name('text-capitalize')
        for div in divs:
            #span=div.find_elements_by_class_name('span')[-1]
            location,appointment=div.text.split('\n')[0],div.text.split('\n')[-1]
            print(location, appointment)
            if location in locations_i_can_go and appointment!='No Appointments Available':

            #if appointment!='No Appointments Available':
                playsound('phone.wav')
                btn=div.find_element_by_tag_name('a')
                btn.click()
                earliest_time=driver.find_element_by_class_name('text-primary')
                earliest_time.click()

            fn=driver.find_element_by_id('firstName')
                fn.send_keys('Xuanyi')

                ln=driver.find_element_by_id('lastName')
                ln.send_keys('Liao')

                email=driver.find_element_by_id('email')
                email.send_keys('zhangliao322@icloud.com')

                phone=driver.find_element_by_id('phone')
                phone.send_keys('2128449360')

                permit_id=driver.find_element_by_id('driverLicense')
                permit_id.send_keys('L40227890003971')

                test=driver.find_element_by_id('test')
                test.send_keys('Auto')

                check_boxes=driver.find_elements_by_id('receiveTexts')
                for check_box in check_boxes:
                    check_box.click()

                submit=driver.find_element_by_xpath('//*[@id="createForm"]/div[1]/div/div[5]/div/div[6]/div[1]/input')
                submit.click()
                return
        print('_'*20)
        time.sleep(5)


get_it_done(driver)


driver.close()