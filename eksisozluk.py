from selenium import webdriver
import random
import time

browser = webdriver.Chrome()

#Website url of the page you want to pull data from
url = "https://eksisozluk.com/titanikin-batis-ani-oldugu-iddia-edilen-video--7420982?a=popular&p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:
    #pages asigned random, 1 is the first and 18 is the last page 
    randomPage = random.randint(1,18)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    #elements picked by css selector of the div content Xpath is still a viable option
    elements = elements = browser.find_elements_by_css_selector("div.content")
    for element in elements:
        entries.append(element.text)
    # time.sleep(2)
    pageCount += 1
with open("entries.txt","w",encoding= "UTF-8") as file:
    for entry in entries:
        file.write(str(pageCount)+"."+ entry +"\n")
        file.write("*************************\n")
        pageCount += 1

# for entry in entries:
#     print(str(entryCount)," **********************")
#     print(entry) 
#     entryCount += 1   

browser.close()