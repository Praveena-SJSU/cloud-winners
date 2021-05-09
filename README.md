# cloud-winners

## DBSetup
CREATE USER 'twitter'@'localhost' IDENTIFIED BY 'tweets';
CREATE DATABASE twitter_sqlalc;
GRANT ALL PRIVILEGES ON twitter_sqlalc.* TO 'twitter'@'localhost';
CREATE TABLE tweets (
    id int primary key not null AUTO_INCREMENT,
    body varchar(1000),
    keyword varchar(256),
    tweet_date datetime,
    location varchar(100),
    verified_user boolean,
    followers int,
    sentiment float
);
 
## Run Script to populate DB
python3 app/run_stream.py -k 'COVID19','Vaccine'

## Run Streamlit for Development
streamlit run app/app.py
