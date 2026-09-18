


from pages.base_page import BasePage


class EventsPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        
        
        #locators
        self.new_event = self.by_test_id("new-event") 
        self.event_name = self.by_id("event-name")
        self.lineup = self.by_id("event-lineup")
        self.start = self.by_id("event-starts")
        self.category = self.by_id("event-category")
        self.venue = self.by_id("event-venue")
        self.create_butt = self.by_test_id("event-save")
        
        
    def go_to_tab(self, tab_name):
        self.click(tab_name)
        
    def create_event(self, event_name, lineup, category, start_date, venue):
         self.click(self.new_event)
         self.fill(self.event_name, event_name)
         self.fill(self.lineup, lineup)
         self.select(self.category, category)
         self.fill(self.start, start_date)
         self.select(self.venue, venue)
         self.click(self.create_butt)
            