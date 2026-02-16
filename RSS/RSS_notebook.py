import feedparser
import os
import pandas as pd

from datetime import datetime

# set the feeds as global variables
ITUNES_Movies = "http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/ws/RSS/topMovies/xml"
ITUNES_Podecasts = "https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.rss"
ITUNES_Books = "https://rss.itunes.apple.com/api/v1/us/books/top-free/all/10/explicit.rss"
# NETFLIX = "http://dvd.netflix.com/Top100RSS"
RSS_LIST = [ITUNES_Movies,ITUNES_Podecasts,ITUNES_Books]

# set the dataframe columns as global variables
DF_COLUMNS = ['source', 'date', 'rank', 'title', 'link', 'summary']


# create a function to parse data and append to a dataframe
def top10_movies(rss, df):
    # parse the feed
    feed = feedparser.parse(rss)

    # check bozo to see if our feed is well formed
    if feed.bozo == 0:
        print("%s is a well-formed feed!" % feed.feed.title)
    else:
        print("%s has flipped the bozo bit. Potential errors ahead!" % feed.feed.title)

    # set the feed date to be the published date, if it exists. If not, use the current date
    feed_date = feed.feed.get('published', datetime.now().strftime('%Y-%m-%d'))

    # set a counter for our loop
    i = 0

    # for the first 10 movies in our feed, append the required information to the dataframe
    while i < 10:
        feed_items = pd.Series([feed.feed.title, feed_date, i + 1, feed.entries[i].title, feed.entries[i].id, \
                                feed.entries[i].summary], DF_COLUMNS)
        df = df.append(feed_items, ignore_index=True)
        i += 1

    # return the dataframe
    return df


if __name__ == "__main__":

    # create an empty dataframe
    top10_df = pd.DataFrame(columns=DF_COLUMNS)
    i = 0
    # run each feed through our top 10 function
    for item in RSS_LIST:
        i += 1
        top10_df = top10_movies(item, top10_df)

    # save the dataframe to a csv. if the csv exists, append to it
    if not os.path.isfile('top10_'+str(i)+'.csv'):
        # top10_df.to_csv('top10_'+str(i)+'.csv', header=DF_COLUMNS, index=False)
    # else:
        top10_df.to_csv('top10_'+str(i)+'.csv', mode='a', header=False, index=False)
