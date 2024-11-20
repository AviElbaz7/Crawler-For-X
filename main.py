"""
Main script to scrape data from Twitter (X) based on the user's requirements.

Features:
- Scrapes tweets based on hashtags (`side=0`).
- Scrapes tweets from specific user timelines (`side=1`).
- Scrapes user following/followers data (`side=3`).

Author: [Your Name]
Date: [Update Date]
"""

import time
import pandas as pd
from WebDriverSetup import setup_web_driver
from SearchScrapper import SearchScrapper
from SearchScrapperDetails import SearchScrapperDetails

def main(side):
    """
    Entry point for scraping tasks.

    Parameters:
    - side (int): Determines the scraping mode.
        - 0: Scrape tweets using hashtags for specific dates.
        - 1: Scrape tweets from user timelines.
        - 3: Scrape following/followers/verified followers of users.
    """
    start_time = time.time()
    driver = setup_web_driver()

    if side == 0:
        # Hashtag scraping
        hashtags = ['hamas']  # Replace or extend this list with relevant hashtags.
        start_date = "2023-11-25"
        end_date = "2023-12-02"
        all_tweets = []

        for hashtag in hashtags:
            search_query = f'https://x.com/search?q=%28%23{hashtag}%29+until%3A{end_date}+since%3A{start_date}&src=typed_query&f=live'
            scraped_tweets = SearchScrapper(driver).scrape_twitter_query(search_query, hashtag, max_tweets=50)

            # Process and format tweet data
            tweets_data = [
                (
                    tweet.ID, tweet.content, tweet.author, tweet.fullName, tweet.url, tweet.timestamp,
                    tweet.image_url, None, None, tweet.video_url, tweet.video_preview_image_url,
                    None, None, None, None, tweet.comments, tweet.retweets, None, tweet.likes,
                    tweet.hashtags, tweet.views, hashtag
                )
                for tweet in scraped_tweets
            ]
            all_tweets.extend(tweets_data)

        # Save results
        columns = [
            'id', 'text', 'username', 'fullname', 'url', 'publication_date', 'photo_url',
            'photo_preview_image_url', 'photo_alt_text', 'video_url', 'video_preview_image_url',
            'video_alt_text', 'animated_gif_url', 'animated_gif_preview_image_url', 'animated_gif_alt_text',
            'replies', 'retweets', 'quotes', 'likes', 'hashtags', 'views', 'target'
        ]
        df = pd.DataFrame(all_tweets, columns=columns)
        df.to_csv(f"{start_date}_to_{end_date}_hashtag_tweets.csv", index=False)
        print(f"Data saved to {start_date}_to_{end_date}_hashtag_tweets.csv")

    elif side == 1:
        # User timeline scraping
        users = ['Cristiano']  # Replace or extend this list with target usernames.
        start_date = "2023-11-25"
        end_date = "2024-02-02"
        all_tweets = []

        for user in users:
            search_query = f'https://x.com/search?q=%28from%3A{user}%29+until%3A{end_date}+since%3A{start_date}&src=typed_query&f=live'
            scraped_tweets = SearchScrapper(driver).scrape_twitter_query(search_query, user, max_tweets=50)

            tweets_data = [
                (
                    tweet.ID, tweet.content, tweet.author, tweet.fullName, tweet.url, tweet.timestamp,
                    tweet.image_url, None, None, tweet.video_url, tweet.video_preview_image_url,
                    None, None, None, None, tweet.comments, tweet.retweets, None, tweet.likes,
                    tweet.hashtags, tweet.views, user
                )
                for tweet in scraped_tweets
            ]
            all_tweets.extend(tweets_data)

        # Save results
        columns = [
            'id', 'text', 'username', 'fullname', 'url', 'publication_date', 'photo_url',
            'photo_preview_image_url', 'photo_alt_text', 'video_url', 'video_preview_image_url',
            'video_alt_text', 'animated_gif_url', 'animated_gif_preview_image_url', 'animated_gif_alt_text',
            'replies', 'retweets', 'quotes', 'likes', 'hashtags', 'views', 'target'
        ]
        df = pd.DataFrame(all_tweets, columns=columns)
        df.to_csv(f"{start_date}_to_{end_date}_user_tweets.csv", index=False)
        print(f"Data saved to {start_date}_to_{end_date}_user_tweets.csv")

    elif side == 3:
        # Followers/following scraping
        users_follows = ['Cristiano']  # Replace or extend this list with target usernames.
        all_follows = []
        follow_types = [
            ("following", "https://x.com/{}/following"),
            ("followers", "https://x.com/{}/followers"),
            ("verified_followers", "https://x.com/{}/verified_followers")
        ]

        for target in users_follows:
            for follow_type, url_template in follow_types:
                url = url_template.format(target)
                scraped_users = SearchScrapperDetails(driver).scrape_following_page(url, max_users=100)

                follows_data = [
                    (target, user.author, follow_type)
                    for user in scraped_users
                ]
                all_follows.extend(follows_data)

        # Save results
        columns = ['target_username', 'other_username', 'type']
        df = pd.DataFrame(all_follows, columns=columns)
        df.to_csv("user_follows.csv", index=False)
        print("Data saved to user_follows.csv")

    else:
        print("Invalid side argument. Use 0 for hashtags, 1 for user timelines, or 3 for user follows.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to run the script: {elapsed_time:.2f} seconds")

if __name__ == '__main__':
    # Replace with the appropriate side argument: 0, 1, or 3
    main(side=0)
