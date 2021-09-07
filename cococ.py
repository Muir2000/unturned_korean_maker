from selenium import webdriver
import time
import os

global lisu
global save
lisu = []
save = []

def search(dirname):
    filename = os.listdir(dirname)
    for filename in filename:
        full_filename = os.path.join(dirname, filename)
        if full_filename.find('.') == True:
            pass
        else:
            lisu.append(full_filename[2:])

def web_trans(titic):
    driver.implicitly_wait(15)
    driver.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea""").clear()
    driver.implicitly_wait(15)
    driver.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea""").send_keys(titic)
    time.sleep(3.2)
    tutu = driver.find_element_by_class_name("""VIiyi""").text
    return tutu

search('./')


path = "C:/Users/JO/Google Drive/한글화한다/304930/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://translate.google.co.kr/?hl=ko&tab=rT")
driver.implicitly_wait(5)

endat = '/English.dat'

for wy in range(0,len(lisu)):
    try:
        data = open('./'+ lisu[wy] + endat,'r',encoding='UTF8')
        print('./'+ lisu[wy] + endat)
        all_data = data.read()
        nanunge = all_data.split('\n')
        Name = nanunge[0][5:]
        Description = nanunge[1][12:]
        save.append(web_trans(Name) + '\n')
        save.append(web_trans(Description).replace("\n","")+'\n')
        data.close()
    except:
        pass
data2 = open('save3.txt','wt',encoding='UTF8')
data2.writelines(save)
data2.close()

driver.close()