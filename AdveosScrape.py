from selenium import webdriver
import time
from fake_useragent import UserAgent

#setup selenium
ua = UserAgent()
a = ua.random
user_agent = ua.random
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--user-data-dir=C:\\Users\30693\\AppData\\Local\\Google\\Chrome\\User Data")#Must be replaced
driver = webdriver.Chrome(executable_path=r'C:\Windows\chromedriver.exe', options=options)#Must be replaced
driver.set_window_size(960, 1280)
#website to scrape
driver.get("https://adveos.com/careers")
time.sleep(5)# mandatory sleep
#data to store
data = {"Positions": [], "Locations": [], "JobsScrape": driver.find_elements_by_class_name('categoryItem')}
for i in range(0,len(data["JobsScrape"])):
    job = driver.find_elements_by_class_name('categoryItem')[i]
    data["Positions"].append(job.text)
    link = job.find_element_by_class_name("categoryItemTitleContainer").find_element_by_xpath("//h2[@class='categoryItemTitle']/a")
    driver.execute_script("arguments[0].click();", link)
    time.sleep(5)
    textToSplit = driver.find_element_by_class_name("articleBody").text
    textSplited = textToSplit.splitlines()
    for item in textSplited:
        if "Location".lower() in item.lower():
            temp = item.split(":")
            data["Locations"].append(temp[1])
            break
    driver.back()
    #print data
for i in range(0, len(data["JobsScrape"])):
    print("Job position %s at %s" % (data["Positions"][i], data["Locations"][i]))

driver.quit()

