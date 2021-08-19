import requests
from bs4 import BeautifulSoup
import json
import time
import random
from playsound import playsound
import gc
import urllib
from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_argument('--headless')
url='http://telegov.njportal.com/njmvc/AppointmentWizard/15'
#url='https://telegov.njportal.com/njmvc/AppointmentWizard/17'
driver = webdriver.Chrome(options=options)
driver.get(url)

locations_i_can_go=set(['North BergenPermits','NewarkPermits','LodiPermits','PatersonPermits','BayonnePermits'])
#make_appoint_ment_now=set(['North BergenPermits','PatersonPermits','BayonnePermits',])
while True:
    driver.refresh()
    html_source=driver.page_source

    page=BeautifulSoup(html_source,'html.parser')
    apps=page.findAll('div',{'class':'text-capitalize'})
    get_out=False
    for div in apps:
        span_i_want=div.findAll('span')[-1]
        span_i_want.id
        location=div.text.split('/')[0]
        #print(span_i_want)
        if location in locations_i_can_go:
            print(div.text)
            if span_i_want.text!='No Appointments Available':
                #if location=='North BergenPermits':
                playsound('phone.wav')
                span_id=span_i_want.attrs['id']
                id_num=span_id[8:]
                btn_id='makebtn'+id_num
                btn=driver.find_element_by_id(btn_id)
                latest_time=driver.find_element_by_class_name('text-primary')
                latest_time.click()

                first_name_input=driver.find_element_by_id('firstName')
                first_name_input.send_keys('Xuanyi')

                last_name_input=driver.find_element_by_id('lastName')
                last_name_input.send_keys('Liao')

                email_input=driver.find_element_by_id('email')
                email_input.send_keys('zhangliao322@icloud.com')

                phone_input=driver.find_element_by_id('phone')
                phone_input.send_keys('2128449360')

                permit_type_input=driver.find_element_by_id('permitType')
                permit_type_input.send_keys('Purchase an auto examination permit (Class D) (ages 17+) ')


                birth_date_input=driver.find_element_by_id('birthDate')
                birth_date_input.send_keys('03/22/1997')

                confirm_boxes=driver.find_elements_by_id('receiveTexts')
                for box in confirm_boxes:
                    box.click()

                submit_btn=driver.find_element_by_xpath('//*[@id="createForm"]/div[1]/div/div[5]/div/div[6]/div[1]/input')
                submit_btn.click()
                get_out=True

    if get_out:
        break
    print('_' * 10)
    time.sleep(5)


driver.close()
    #print(span_i_want.text)
# def find(res_json):
#     available_locations=[]
#     for r in res_json:
#         available=r['LocAppointments'][0]['AppointmentType']
#         if available:
#             available_locations.append(r)
#             playsound('phone.wav')
#     return available_locations
#
#
# while True:
#     try:
#         page=requests.get(headers=headers,url=url)
#         soup = BeautifulSoup(page.text, "html.parser")
#
#         # tree=html.fromstring(soup.getText())
#         # res=tree.xpath('//*[@id="locationsDiv"]')
#
#         x=soup.find_all('script')[21]
#         x=x.contents[0]
#         x=str(x).split('//')[0].split('=')[1].split('\r\n')[0].strip()[:-1]
#
#         res_json=json.loads(x)
#         print(res_json)
#         break
#         available_locations=find(res_json)
#         if available_locations:
#             print('*'*20)
#             print(time.asctime(), ' Find!!!!!!!!')
#             print(available_locations)
#             print('*' * 20)
#             break
#         sec = random.randint(30,90)
#         print(time.asctime(), f' Not Found, check it in {sec} seconds ')
#         time.sleep(sec)
#         gc.collect()
#     except:
#         playsound('phone.wav')
#         break