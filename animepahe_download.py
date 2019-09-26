from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options() 
#change it according to IDM crx file else comment out if no IDM 
options.add_extension("C:/Program Files (x86)/Internet Download Manager/IDM-extension.crx")

#change it according to your chromedriver location
chrome_driver = "D:\\Downloads\\Programs\\chromedriver.exe"

#use it if you don't have IDM
#driver = webdriver.Chrome(chrome_driver)

#use the below 4 lines if you have IDM else put # infront of the below 3 lines and remove the # from above line 
driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=options)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

#link of the starting address of the episode to be downloaded
link = 'https://animepahe.com/play/one-piece/f70e63527b56af5763c96f638bab8b797dc30a68'

anime_main = 'https://animepahe.com'

#number of episodes to download from current one
no_of_episodes = 3

next_page = link;

#fetch links from every page and download
for episodes in range(0,no_of_episodes):
    driver.switch_to.window(driver.window_handles[0])
    driver.get(next_page)
    time.sleep(2)
    container = driver.find_element_by_id('pickDownload')
    link = container.find_element_by_css_selector('a').get_attribute('href')
    
    while(link==None):#wait for 
        link = container.find_element_by_css_selector('a').get_attribute('href')
    #print(link)
    container = driver.find_element_by_xpath('//*[@title="Play Next Episode"]')
    next_page = container.get_attribute('href')#store link of next page
    
    container = driver.find_element_by_id('downloadMenu')
    container.click()#click on download dropdown
    container = driver.find_element_by_id('pickDownload')
    main_page = driver.window_handles[0]
    container.click()#click on download new pop up tab opens
    time.sleep(3)
    #switch focus to new opened tab
    down_page = driver.window_handles[1]

    for i in range(0,len(driver.window_handles)):
        if(i<len(driver.window_handles)):
            driver.switch_to.window(driver.window_handles[i])
        
        if(i<len(driver.window_handles)):
            url = driver.current_url
            if(url[8]=='k'):
                down_page = driver.window_handles[i]
    
    driver.switch_to.window(down_page)
    
    container = driver.find_element_by_xpath('//*[@class="fas fa-download"]')
    container.click();
    time.sleep(1)
    
    for i in reversed(range(1,len(driver.window_handles))):
        if(i<len(driver.window_handles)):
            driver.switch_to.window(driver.window_handles[i])
        
        if(i<len(driver.window_handles)):
            url = driver.current_url
            driver.close()
    
    driver.switch_to.window(driver.window_handles[0])
   
driver.close()
