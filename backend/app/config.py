import os


class TwitterConfig:
    CONSUMER_KEY = '6PMM2nBxsGzUMLrpVuR1aNDib'
    CONSUMER_SECRET = 'l5YARUIQfkooaIuinR3skMMJ0CI3Lok6eOHEYiUaW7MpLZCuSj'
    ACCESS_TOKEN = '1378132309677809668-pymEJH7NafhERv4fzi8ymCa42TXC3x'
    ACCESS_TOKEN_SECRET = 'ElGMxtD7DCs0nUvLgAlyUNmaePADcxzQ6fsiBIGegLNZM'


class DBConfig:
    # USER = os.environ.get('DB_USER')
    # PWORD = os.environ.get('DB_PWORD')
    # HOST = os.environ.get('DB_HOST')
    USER = "twitter"
    PWORD = "tweets"
    HOST = "localhost"


if __name__ == '__main__':
    print(type(os.environ.get('CONSUMER_KEY')))