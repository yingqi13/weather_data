#from bs4 import BeautifulSoup
#import requests

#response = requests.get("https://en.wikipedia.org/wiki/JavaScript")

#webpage = response.text

#soup = BeautifulSoup(webpage, "html.parser")
#print(soup.find("td", class_="ng-star-inserted"))
#data = soup.select("td.ng-star-inserted")
#print(data)
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from date_list import full_dates
from csv import writer

driver = webdriver.Chrome('/Users/yingqi/Desktop/chromedriver')

for date in full_dates:
    link = f'https://www.wunderground.com/history/daily/OTBD/date/{date}'
    driver.get(link)
    #sleep time ensures that there is sufficient time for website to load
    sleep(5)
    high_temp = float(driver.find_element(By.XPATH, "/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[1]/td[1]").text)
    low_temp = float(driver.find_element(By.XPATH, "/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[2]/td[1]").text)
    average_temp = float(driver.find_element(By.XPATH, "/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[3]/td[1]").text)
    CDD_HDD = float(average_temp - 65)
    values = [date, high_temp, low_temp, average_temp, CDD_HDD]
    with open('daily_weather_CDDHDD.csv', 'a') as file:
        writer_object = writer(file)
        writer_object.writerow(values)
        file.close()







