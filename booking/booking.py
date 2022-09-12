import booking.constants as const
from booking.booking_filteration import BookingFilteration
from booking.booking_report import BookingReport
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"/drivers/", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] = os.getcwd()
        os.environ['PATH'] += self.driver_path
        print(os.environ['PATH'])
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency_element = self.find_element(By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_places_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(By.ID, 'xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()
            adults_count = int(self.find_element(By.ID, 'group_adults').get_attribute('value'))
            if adults_count == 1:
                break
        
        increase_button_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filterations(self):
        filteration = BookingFilteration(driver = self)
        filteration.apply_star_rating(star_value = 3)

    def report_results(self):
        hotel_boxes = self.find_element(By.CLASS_NAME, 'dcf496a7b9')
        # hotel_cards = hotel_boxes.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        report = BookingReport(hotel_boxes)
        print(report.pull_titles())
        

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

