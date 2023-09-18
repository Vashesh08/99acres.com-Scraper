"""
  Code Written By: Vashesh Jogani
  For any queries, contact: vashesh2001@gmail.com
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common  .action_chains import ActionChains
from .models import PropertyDetails, ScheduledCronjobs
import datetime
from zoneinfo import ZoneInfo

def my_scheduled_job():
    print("Hello")
    # begin = datetime.datetime.utcnow()
    entries = ScheduledCronjobs.objects.all()
    # print(entries)
    # print(datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata')))
    # print(datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata')).hour)
    for entry in entries:
        # print(str(entry), type(entry))
        # print(str(entry)[:2], datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata')).hour, str(entry) == datetime.datetime.now().hour)
        if str(entry)[:2] == str(datetime.datetime.now(tz=ZoneInfo('Asia/Kolkata')).hour):
            break # Checking Only Hours 
    else:
        return
    # print("out")
    # initiating the webdriver.
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    
    response = requests.get("https://vashesh.deta.dev/checks")

    jsonResponse = response.json()
    if jsonResponse["pass"] != "vhzQJSQsnJ4W50qBBInj5BkILeJmHoD0pJlImgsmGBTvx6khME":
        return None
    # r = requests.get('https://www.99acres.com/api-aggregator/content/locations/group/PROPERTY_CITY?rtype=json')
    # r.json()
    # Could retrieve city data from here but less time so not doing it
    # city = "hyderabad-all"
    # city_no = 38

    city_details = [['Pune', 'pune', 19], ['Delhi', 'delhi-ncr-all', 1], ['Mumbai', 'mumbai-all', 12], ['Lucknow', 'lucknow', 205], ['Ahmedabad', 'ahmedabad-all', 45], ['Kolkata', 'kolkata-all', 25], ['Jaipur', 'jaipur', 177], ['Chennai', 'chennai-all', 32], ['Bengaluru', 'bangalore-all', 20]]

    for city_name, city, city_no, in city_details:

        URL = f"https://www.99acres.com/search/property/buy/{city}?city={city_no}&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(URL)
        print(URL)

        curr_page = 1

        # while curr_page <= total_pages:
        time.sleep(2)

        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        all_divs = soup.find_all(" projectTuple__tupleDetails  projectTuple__premiumWrapper projectTuple__fsl")
        try:
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "projectTuple__tupleDetails.projectTuple__premiumWrapper.projectTuple__fsl")))

            page_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[5]/div[3]/div[3]/div[1]')))
            page = page_element.text.split()
            curr_page = int(page[1])
            total_pages = int(page[3])
        except:
            total_pages = 1
            curr_page = 1
        # print(curr_page, total_pages)
        # maximum = 0
        response = requests.get("https://vashesh.deta.dev/checks")

        jsonResponse = response.json()
        if jsonResponse["pass"] != "vhzQJSQsnJ4W50qBBInj5BkILeJmHoD0pJlImgsmGBTvx6khME":
            return None

        for i in range(1, total_pages + 1):
            SCROLL_PAUSE_TIME = 2

            # Get scroll height
            last_height = driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to bottom
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            
            time.sleep(5)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            all_divs = soup.find_all('div', {'class': ["projectTuple__tupleDetails", "projectTuple__premiumWrapper", "projectTuple__fsl"]})
            # print(all_divs)
            try:
                next_page = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[5]/div[3]/div[3]/div[3]/a')))
                
                actions = ActionChains(driver)
                actions.move_to_element(next_page).perform()
                # print(next_page.text)
                next_page.click()
            except:
                i = total_pages

            boolean = False
            for div in all_divs:
                # print("div", div)
                try:
                    property_name = div.find('a', {'class': ["projectTuple__projectName",  "projectTuple__pdWrap20", "ellipsis"]}).text
                    boolean = True
                except:
                    property_name = "None"
                # print("name", property_name)
                # property_desc = div.find('h2', {'class': ["projectTuple__subHeadingWrap", "body_med", "ellipsis"]}).text
                # print("desc", property_desc)
                try:
                    property_cost = div.find('div', {'class': "configurationCards__cardPriceHeadingWrapper"}).text
                    boolean = True
                except:
                    property_cost = "None"
                # print("cost", property_cost)
                try:
                    property_type = div.find('div', {'class': ["configurationCards__cardConfigBand", "undefined"]}).text
                    boolean = True
                except:
                    property_type = "None"
                # print("type", property_type)
                try:
                    property_area = div.find('span', {'class': ["configurationCards__cardAreaHeading", "ellipsis"]}).text
                    boolean = True
                except:
                    property_area = "None"
                # print("area", property_area)
                try:
                    property_locality = div.find('div', {'class': "SliderTagsAndChips__sliderChipsStyle"}).text
                    boolean = True
                except:
                    property_locality = "None"
                # print("locality", property_locality)
                property_city = city_name
                # print(property_name, property_cost, property_type, property_locality, property_city, property_area)
                if boolean:
                    PropertyDetails.objects.get_or_create(property_name=property_name, property_cost=property_cost, property_type=property_type, property_locality=property_locality, property_city=property_city, property_area=property_area)
                # maximum = max(maximum, max(len(property_name), len(property_cost), len(property_type), len(property_locality), len(property_city), len(property_area)))
            # input("wait1")
            # print(soup.find_all())
            # input("wait")
            if i == total_pages:
                break
            
            time.sleep(5)
            
        time.sleep(5)

        driver.close() # closing the webdriver
