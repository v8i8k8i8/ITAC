
from pages.base_page import BasePage



class LoginPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        
        
        #locators
    
        self.email = self.by_id("email")
        self.password = self.by_id("password")
        self.login_butt = self.by_test_id("login-submit")    
    
    def login(self, email, password):
        self.fill(self.email, email)
        self.fill(self.password, password)
        self.click(self.login_butt)
        