"""
Author: Andrew Stocker
Description: scrapes and number of submissions in a given subreddit
Input: arg1= subreddit id and arg2= # of submissions
Run: python bulk_scrape arg1 arg2
"""
import praw
from scraper import get_reddit_client, pkl_thread

from sys import argv


def bulk_scrape(submissions):
  for t in submissions:
    pkl_thread(t)


if __name__=="__main__":
  R = get_reddit_client()
  
  subreddit_id = argv[1] #example: www.reddit.com/r/cars use "cars"
  limit = int(argv[2]) #number of submissions to scrape
  
  submissions = R.get_subreddit(subreddit_id).get_hot(limit=limit)
  
  bulk_scrape(submissions)
  
