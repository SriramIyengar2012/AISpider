
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import random


class Browser():
     
    def __init__(self):
        self.dict = {"test": ["1", "2"], "test2": ["1", "2"] }
        self.elems_list = []
        self.page_elems_list = []
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path="/Users/sriramiyengar/Documents/hackathontest/getXpath/chromedriver")
    
    def navigate(self):  
        #self.data();    
        self.driver.get('')
        self.driver.find_element_by_link_text("").click()
        self.driver.find_element_by_name("").send_keys("")
        self.driver.find_element_by_name("").clear
        self.driver.find_element_by_name("").send_keys("")
        self.driver.find_element_by_xpath("").click()
        time.sleep(10)   
        #self.driver.find_element_by_link_text("Dismiss").click()
        elems = self.driver.find_elements_by_tag_name("a")
        for elem in elems:
            print("IN Navigate")
            print(elem.get_attribute('href'))
            if elem.get_attribute('href') is not None:
                self.elems_list.append(elem.get_attribute('href'))
           
        for el in self.elems_list:
                self.crawl(el)    
         
    def crawl(self, url):
        print("IN Crawl")       
        try: 
           print("&&")      
           self.driver.get(url)
           self.driver.implicitly_wait(10)
           #WebDriverWait(self.driver, 5).until(EC.url_changes(url))
           print("****")
           self.set_attribute()  
           self.button_exists()
           elements = self.driver.find_elements_by_tag_name("a")
           for elem in elements:
                if elem.get_attribute('href') is not None:
                    self.page_elems_list.append(elem.get_attribute('href'))
           for el in self.page_elems_list:
               self.click_links(el) 
                   
        except:
            pass

    def click_links(self, url):
        self.driver.get(url) 
        self.driver.implicitly_wait(10)
        self.set_attribute()   
        self.driver.implicitly_wait(10)


    def check_exists(self, text):
       try:
          self.driver.find_element_by_link_text(text)
       except NoSuchElementException:
           return False
       return True   

    def element_exists(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True  

    def element_exists(self, attr,element):
        try:
            value = element.get_attribute(attr)
        except:
            return False
        return True          
                

    def input_box_enter_values(self):
        try:
            textbox = self.driver.find_elements_by_xpath("//input[@type='text']")
            try:
              for txt in range(len(textbox)-1):
                if self.element_exists(txt.find_element("following-sibling::label")) == True:
                    label_attr = txt.find_element("following-sibling::label").get_attribute("for")
                    value = self.data(label_attr)
                    txt.send_keys(value)
                elif self.element_exists(txt.find_element("preceding-sibling::label")) == True:
                     label_attr = txt.find_element("preceding-sibling::label").get_attribute("for")
                     value = self.data(label_attr)
                     txt.send_keys(value)
                elif self.input_exists(txt,'aria-label') == True:
                     label_attr = txt.get_attribute('aria-label')
                     value = self.data(label_attr)
                     txt.send_keys(value)  
            except:
                pass                                      
        except NoSuchElementException:
            pass        

    def data(self, column):
        data = pd.DataFrame(self.dict)
        random_num = self.get_random_number()
        print(data.iloc[random_num][column])
        return data.iloc[random_num][column]

    def set_attribute(self):
        print("$$$$")
        checkbox = self.driver.find_elements_by_xpath("//input[@type='checkbox']")
        print(len(checkbox))
        for ck in checkbox:
            print("££")
            #ck.click()
            self.driver.execute_script("arguments[0].setAttribute('checked', 'checked')",ck)
            self.driver.implicitly_wait(10)
           

    def button_exists(self):
        button_ele = self.driver.find_elements_by_tag_name('button')
        for bt in button_ele:
            bt.click()
            self.driver.implicitly_wait(10)
    
    def get_random_number(self):
        print(random.randrange(1, 10, 2))
        num = random.randrange(1, 10, 2)
        return num


run = Browser()
run.navigate()
          
            
        
        

  