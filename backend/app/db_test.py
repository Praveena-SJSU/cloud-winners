import pymysql.cursors
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import session_scope, init_db

from config import DBConfig
from models import Tweet

import pandas as pd
import datetime


# engine = create_engine('mysql+pymysql://{}:{}@{}/twitter_sqlalc'.format(DBConfig.USER, DBConfig.PWORD, DBConfig.HOST),
#                        convert_unicode=True)


def print_tables_stats():
    print(posts.columns)         # return a list of columns
    print(posts.c)               # same as posts.columns
    print(posts.foreign_keys)    # returns a set containing foreign keys on the table
    print(posts.primary_key)     # returns the primary key of the table
    print(posts.metadata)        # get the MetaData object from the table
    print(posts.columns.post_title.name)     # returns the name of the column
    print(posts.columns.post_title.type)     # returns the type of the column

def create_tweet():
    tweet = Tweet(body="covid19 will go away", 
            keyword="covid19", 
            tweet_date=datetime.datetime.now(), 
            location="india",
            verified_user=True, 
            followers=100,
            sentiment=0.5)
    tweet.id = '2'
    return tweet

def set_data(tweet):
    Session = sessionmaker(bind=engine)

    # create a Session
    sess = Session()

    print("Tweet3: " + tweet.body)
    sess.add(tweet)
    sess.commit()
    sess.close()        

def get_data():
    timestamp = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    if engine is not None:
        print("reading sql table")
        df = pd.read_sql_table('tweets', engine)
        df = df.rename(columns={'body': 'Tweet', 'tweet_date': 'Timestamp',
                            'followers': 'Followers', 'sentiment': 'Sentiment',
                            'keyword': 'Subject'})
        print(df)
    return df, timestamp

init_db()
set_data(create_tweet())
df, ts = get_data()
print(df)
