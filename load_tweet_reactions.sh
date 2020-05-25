#!/bin/bash

initial_tweet_id=$1

mkdir out/${initial_tweet_id}
mkdir out/${initial_tweet_id}/media
mkdir out/${initial_tweet_id}/raw_tweets

twarc replies ${initial_tweet_id} > out/${initial_tweet_id}/raw_tweets/replies_${initial_tweet_id}.jsonl --recursive
twarc search ${initial_tweet_id} > out/${initial_tweet_id}/raw_tweets/search.jsonl

python get_quoted_ids.py \
        --inf out/${initial_tweet_id}/raw_tweets/search.jsonl \
        --outf out/${initial_tweet_id}/get_replies_of_quoted.sh \
        --outformat "twarc replies {id_} > "out/${initial_tweet_id}/"raw_tweets/replies_{id_}.jsonl --recursive"

chmod u+x out/${initial_tweet_id}/get_replies_of_quoted.sh
out/${initial_tweet_id}/get_replies_of_quoted.sh

python combine_datasets.py \
        --indir out/${initial_tweet_id}/raw_tweets/ \
        --outpath out/${initial_tweet_id}/raw_tweets/combined.jsonl

python load_images.py \
         --inpath out/${initial_tweet_id}/raw_tweets/combined.jsonl \
         --outdir out/${initial_tweet_id}/media/