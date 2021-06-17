import pytest
import time


class TestMain:
    def test_language_on_site(self, browser):
        """Test language on site http://selenium1py.pythonanywhere.com"""
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(3)
        assert browser.find_elements_by_xpath("//form//button[contains(@class, 'btn-lg')]"), 'Button not found!'
