from selenium.webdriver.common.by import By
from selenium import webdriver
from typing import List

class BookingFilteration:
    def __init__(self, driver):
        self.driver = driver

    def apply_star_rating(self, star_value):
        for i in range(3, 15, 2):
            star_child_elements = self.driver.find_element(By.XPATH, f"/html[1]/body[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[{i}]/label[1]/span[3]/div[1]/div[1]/div[1]/div[1]/div[1]")
            star_child_value = star_child_elements.get_attribute("innerHTML").strip()
            if str(star_child_value) == f'{star_value} stars':
                star_child_box_element = self.driver.find_element(By.XPATH, f"/html[1]/body[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[{i}]/label[1]/span[2]")
                break
        star_child_box_element.click()

        