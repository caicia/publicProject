from selenium import webdriver
import time

def get_data():
    pass
    #根据具体产品进行修改获取内容

def crawler():
    browser.get('https://www.tmall.com/')
    time.sleep(5)
    search = browser.find_element_by_id('mq')
    search.send_keys(key_word)
    search_button = browser.find_element_by_xpath('//*[@type="submit"]')
    search_button.click()



if __name__ == '__main__':
    key_word = '车厘子'
    browser = webdriver.Chrome("./chromedriver")
    crawler()
