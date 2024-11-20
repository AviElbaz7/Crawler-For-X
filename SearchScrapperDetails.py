"""
Module for scraping user details (followers/following/verified followers) on Twitter (X) using Selenium WebDriver.

Classes:
- UserDetail: Represents details of a user (username).
- SearchScrapperDetails: Handles scraping of user followers and following lists.

Author: [Your Name]
Date: [Update Date]
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from time import sleep
import random

class UserDetail:
    """
    Represents a user's basic details.

    Attributes:
    - author: Username of the user (e.g., @handle).
    """
    def __init__(self, author):
        self.author = author

    def __repr__(self):
        return f'UserDetail({self.author})'

    def __eq__(self, other):
        return isinstance(other, UserDetail) and self.author == other.author

    def __hash__(self):
        return hash(self.author)

class SearchScrapperDetails:
    """
    Scraper for Twitter (X) user details (followers/following).

    Methods:
    - scrape_following_page(query_url, max_users): Scrapes a list of users from a given Twitter page.
    """
    def __init__(self, driver: webdriver.Chrome):
        """
        Initializes the scraper with a Selenium WebDriver instance.

        Parameters:
        - driver (webdriver.Chrome): The Selenium WebDriver instance.
        """
        self.driver = driver

    def scrape_following_page(self, query_url: str, max_users: int):
        """
        Scrapes user details from a Twitter followers/following page.

        Parameters:
        - query_url (str): URL of the followers/following page to scrape.
        - max_users (int): Maximum number of users to scrape.

        Returns:
        - set[UserDetail]: A set of UserDetail objects containing scraped user data.
        """
        self.driver.get(query_url)
        retries = 3
        user_details = set()
        processed_elements = set()

        # Check if the page has no users
        for _ in range(retries):
            try:
                empty_state_element = self.driver.find_element(By.XPATH, '//div[@data-testid="emptyState"]')
                print("No users found on this page.")
                return set()
            except (NoSuchElementException, StaleElementReferenceException):
                sleep(0.5)

        # Wait for user list to load
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//button[@data-testid="UserCell"]'))
            )
        except TimeoutException:
            print("Timeout: No users found on the page after waiting.")
            return set()

        print("Scraping users...")
        prev_height = self.driver.execute_script('return document.body.scrollHeight')
        no_new_content_attempts = 0

        while len(user_details) < max_users:
            try:
                loaded_users = self.driver.find_elements(By.XPATH, '//button[@data-testid="UserCell"]')

                for user_element in loaded_users:
                    element_id = user_element.id
                    if element_id in processed_elements:
                        continue

                    try:
                        # Extract username
                        author = user_element.find_element(By.XPATH, './/span[contains(text(), "@")]').text.replace("@", "")
                        user_details.add(UserDetail(author=author))
                        processed_elements.add(element_id)
                    except NoSuchElementException:
                        pass

                if len(user_details) >= max_users:
                    break

                # Scroll to load more users
                scroll_distance = random.uniform(700, 1000)
                self.driver.execute_script(f'window.scrollBy(0, {scroll_distance})')
                sleep(random.uniform(1, 3))

                curr_height = self.driver.execute_script('return document.body.scrollHeight')
                if curr_height == prev_height:
                    no_new_content_attempts += 1
                    if no_new_content_attempts >= 20:
                        break
                else:
                    no_new_content_attempts = 0

                prev_height = curr_height

            except StaleElementReferenceException:
                pass

        print("Scraping complete.")
        return user_details
