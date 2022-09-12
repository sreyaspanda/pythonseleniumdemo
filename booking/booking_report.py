from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def pull_titles(self):
        hotel_list = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(By.CSS_SELECTOR, 'a[data-testid="title-link"] > div[data-testid="title"]').get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="price-and-discounted-price"] > span[class="fcab3ed991 bd73d13072"]').get_attribute('innerHTML').strip()
            hotel_list.append([hotel_name, hotel_price])
        return hotel_list

