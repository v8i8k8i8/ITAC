
from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def open(self, url: str):
        self.page.goto(url)
        
    
    #locators
    
    def by_id(self, element_id:str) -> Locator:
        return self.page.locator(f"#{element_id}")
    
    def by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)
    
    def by_text(self, text: str) -> Locator:
        return self.page.get_by_text(text)
        
    
    
    
    #actions    
         
    def fill(self, locator: Locator, text: str):
         locator.fill(text)  
         
    def click(self, locator: Locator):
        locator.click()       
        
    def select(self, locator: Locator, value:str):
        locator.select_option(value)    
           