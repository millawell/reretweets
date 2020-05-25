# crawl replies and retweets with comments (quotes) of a tweet
## Usage
Most importantly, downloading the tweets can be done by
```
./load_tweet_reactions.sh $TWEET_ID
```

To combine and unique downloaded tweets, you can use
the `combine_datasets.py`, for converting to tsv, you can use `to_tsv.py`.


## Functionality

The script takes the following steps to obtain tweets and quotes:

1. It downloads all direct replies (recursively) to the tweet
2. It searches for the tweet id, to get quotes
3. For each tweet, that quoted the original tweet, it again retrieves all replies.

## Requirements
python packages:

* click
* tqdm
* pandas
* twarc