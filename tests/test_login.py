

from playwright.sync_api import expect

from pages.login_page import LoginPage
from configs.config import config


def test_login(page):
    
    login_page = LoginPage(page)
    login_page.open(config["url"])
    login_page.login(
        config["cred"]["user"],
        config["cred"]["pass"]
    )
    
    expect(page).to_have_url("https://arena.itac.co.il/events")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="reports/success_login.png", full_page = True)
    