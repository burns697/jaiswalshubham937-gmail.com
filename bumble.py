#importing libraries
from selenium import webdriver
from time import sleep

class BumbleBot():
    """
    version =0.1 
    bot for swiping on bumble 
    inspired 0rion5 tinder bot
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self,number,password):
        self.driver.get('https://bumble.com/')
        sleep(2)
        log_btn=self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        log_btn.click()
        sleep(3)
        log_btn2=self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[3]/div/span/span')
        log_btn2.click()
         # switch to login popup
        base_window = self.driver.window_handles[0]
        num_in = self.driver.find_element_by_xpath('//*[@id="phone"]')
        num_in.send_keys(number)
        log_btn3=self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[4]/button/span/span')
        log_btn3.click()
        sleep(2)
        pass_in=self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)
        log_btn4=self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[2]/button/span/span')
        log_btn4.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/span/span')
        like_btn.click()
    
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/span/span')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.like()
            except Exception:
                print("something is wrong bruv")

if __name__ == "__main__":
    t=BumbleBot()
    t.login('phone number','password')
    t.auto_swipe()