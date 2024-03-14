import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

ch=input("Are you doing a follow up consulation?: ")


class Browser:
    browser,service = None,None

    def __init__(self,driver:str):
        self.service=Service(driver)
        self.browser= webdriver.Chrome(service=self.service, options =chrome_options)
        self.wait = WebDriverWait(self.browser, 10)

    def open_page(self, url:str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self,by:By,value:str,text:str):
        try:
            field = self.wait.until(EC.presence_of_element_located((by, value)))
            field.send_keys(text)
            time.sleep(1)
        except selenium.common.exceptions.TimeoutException:
            print(f"Element not found: {by}, {value}")

    def click_button(self, by:By, value:str):
        try:
            button = self.wait.until(EC.element_to_be_clickable((by, value)))
            button.click()
            time.sleep(1)
        except selenium.common.exceptions.TimeoutException:
            print(f"Element not clickable: {by}, {value}")

    def login(self,username:str,password:str):
        self.add_input(by=By.ID,value='mat-input-2',text=username)
        self.add_input(by=By.ID,value='mat-input-3',text=password)

    def oneinput(self,tex:str,val:str):
        self.add_input(by=By.CLASS_NAME,value=val,text=tex)
    
    def exec_script(self,by:By, path:str):
        element_to_scroll_to = self.browser.find_element(by,path)  
        self.browser.execute_script("arguments[0].scrollIntoView();",element_to_scroll_to)
        time.sleep(2)

    def scrollup(self):
        self.browser.execute_script("window.scrollTo(0, 0);")

    def scrolldown(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

if __name__ == '__main__':
    browser = Browser('C:\driver\chromedriver.exe')
    browser.open_page('https://esanjeevani.mohfw.gov.in/#/patient/signin')
    time.sleep(5)


    browser.click_button(By.CSS_SELECTOR, 'button[translate="login.passwordFieldLabel"]')
    
    browser.click_button(By.ID,"mat-select-value-1")
    browser.click_button(By.ID,"mat-option-0")
    browser.login("akeshav0601@gmail.com","Ultrainstinct09!")
    time.sleep(5)

    browser.exec_script(By.CSS_SELECTOR,'button[translate="login.loginButton"]')
    browser.click_button(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/form/div[4]/div/button')
    time.sleep(5)

    #browser.oneinput("9092093628",'/html/body/app-root/app-outer-layout/app-signin/div/div/div/div[1]/form/div/div/mat-tab-group/div/mat-tab-body[1]/div/form/div[2]/mat-form-field/div/div[1]/div[3]/input')
    #browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    browser.scrollup()
    time.sleep(3)
    
    browser.click_button(By.XPATH,'//*[@id="main-body"]/app-root/app-patient-layout/patient-header/nav/div/div[2]/div/ul/li[1]/a/mat-icon')
    time.sleep(5)

    #browser.scrollup()

    '''if(ch=='y'):
        browser.exec_script(By.CSS_SELECTOR,'#mat-radio-13')
        browser.click_button(By.CSS_SELECTOR,'#mat-radio-13')
    else:
        browser.exec_script(By.CSS_SELECTOR,'#mat-radio-14')
        browser.click_button(By.CSS_SELECTOR,'#mat-radio-14')
    time.sleep(5)'''

    browser.oneinput('common cold','searchText_input')
    time.sleep(5)

    '''browser.exec_script(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div[3]/span')
    browser.click_button(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div[3]/span')
    time.sleep(5)

    browser.exec_script(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div[4]/img')
    browser.click_button(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div[4]/img')
    time.sleep(5)

    browser.exec_script(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]/input')
    browser.oneinput('sore throat and cold','/html/body/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]/input')
    time.sleep(5)

    browser.exec_script(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div[2]/span')
    browser.click_button(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div[2]/span')
    time.sleep(5)

    browser.exec_script(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div/div[2]/span')
    browser.click_button(By.XPATH,'/html/body/div/div/div/div/div/div[1]/div[2]/div/div[2]/span')'''

    
    


