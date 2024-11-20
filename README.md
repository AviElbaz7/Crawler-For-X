# Twitter Scraper

A Python-based scraper for extracting data from Twitter (X) using Selenium WebDriver. The scraper supports three main functionalities: scraping tweets based on hashtags, user timelines, and user followers/following data.

## Features

- **Hashtag Scraping (`side=0`)**
  - Scrape tweets associated with specific hashtags within a date range.
  
- **User Timeline Scraping (`side=1`)**
  - Scrape tweets from the timelines of specific users within a date range.
  
- **Followers/Following Scraping (`side=3`)**
  - Scrape the followers, following, and verified followers of specific users.

## Prerequisites

1. **Python 3.8+**
   - Ensure Python is installed on your system.
   
2. **Selenium**
   - Install the Selenium library for Python:
     ```bash
     pip install selenium
     ```

3. **WebDriver Manager**
   - Use WebDriver Manager to manage the ChromeDriver:
     ```bash
     pip install webdriver-manager
     ```

4. **Pandas**
   - Install Pandas for data manipulation:
     ```bash
     pip install pandas
     ```

5. **Google Chrome**
   - Ensure Google Chrome is installed on your system.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/twitter-scraper.git
   cd twitter-scraper

2. **Setup**
   - Place your Twitter credentials in `WebDriverSetup.py` for the login process.
   - Ensure the Selenium WebDriver setup is complete.

## File Overview

- **`main.py`**
  - Entry point for the program. Allows the user to choose a scraping mode (`side=0`, `side=1`, or `side=3`).

- **`SearchScrapper.py`**
  - Handles the logic for scraping tweets using hashtags and user timelines.

- **`SearchScrapperDetails.py`**
  - Handles the logic for scraping user followers and following lists.

- **`WebDriverSetup.py`**
  - Configures and initializes the Selenium WebDriver for scraping Twitter.

## Usage

1. **Run the Program**
   - Open a terminal in the project directory and run:
     ```bash
     python main.py
     ```

2. **Choose a Scraping Mode**
   - Set the `side` parameter in `main.py`:
     - `side=0`: Scrape tweets using hashtags.
     - `side=1`: Scrape tweets from user timelines.
     - `side=3`: Scrape followers/following data for users.

3. **View Results**
   - Results are saved as CSV files in the project directory:
     - Hashtag tweets: `<start_date>_to_<end_date>_hashtag_tweets.csv`
     - User tweets: `<start_date>_to_<end_date>_user_tweets.csv`
     - Followers/Following: `user_follows.csv`

## Example

### Scraping Tweets Using Hashtags
1. Set `side=0` in `main.py`.
2. Specify hashtags, start date, and end date.
3. Run the program to generate a CSV of tweets for the specified hashtags.

### Scraping User Timelines
1. Set `side=1` in `main.py`.
2. Specify usernames, start date, and end date.
3. Run the program to generate a CSV of tweets from the specified user timelines.

### Scraping Followers/Following
1. Set `side=3` in `main.py`.
2. Specify usernames to scrape their followers or following data.
3. Run the program to generate a CSV of the user’s follower/following lists.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request for review.
