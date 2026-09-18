


from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.events_page import EventsPage
from configs.config import config

    
def test_create_event(page):   
    login_page = LoginPage(page)
    login_page.open(config["url"])
    login_page.login(
        config["cred"]["user"],
        config["cred"]["pass"]
    )
    
    expect(page).to_have_url("https://arena.itac.co.il/events")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="reports/success_login.png", full_page = True)
    
        #locators
    admin = page.get_by_test_id("nav-admin") 
    
    
    event_name = "new event 6666aaaa"
    lineup = "lineup 13aaa"
    category = "Comedy"
    start_date = "2026-09-28T20:16"
    venue = "9b3e9fef-2d2c-4a68-86bd-0da1eca58bb0"  # Tel Aviv
    
    events_page = EventsPage(page)
    events_page.go_to_tab(admin)
    events_page.create_event(event_name, lineup, category, start_date, venue)
    expect(page.get_by_text(event_name)).to_be_visible()
    page.wait_for_load_state("networkidle")
    page.screenshot(path="reports/success_event.png", full_page = True)