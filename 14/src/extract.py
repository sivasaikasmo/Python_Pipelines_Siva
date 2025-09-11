# Extract
# Use the Twitter API (v2) to collect recent tweets containing a specific hashtag (e.g., #BrandCampaign).
# Collect key fields:
# tweet_id
# created_at
# text
# author_id
# retweet_count
# like_count

import requests
import pandas as pd

def extract():
    HASHTAG='CashAppFriday'
    bearer_token='AAAAAAAAAAAAAAAAAAAAAI3t3wEAAAAAtkjvYOAUShuuGH4dpy4FBb1%2Bw7w%3DCCtHiWSOkktQhXEsjYn1Z3dx2EWkf4OnPXmbHZSMXBaDHA1JFX'
    SEARCH_URL=r'https://api.twitter.com/2/tweets/search/recent'
    headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
    }
    params = {
    'query': HASHTAG,
    'tweet.fields': 'tweet_id,created_at,text,author_id,retweet_count,like_count',
    'max_results': 10
    }
    response = requests.get(SEARCH_URL, headers=headers, params=params)
    print(response)
    # data=[{'public_metrics': {'retweet_count': 0, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 0}, 'text': 'Is it over 😭 #CashAppFriday https://t.co/QcjObIICX0', 'author_id': '1280761062', 'created_at': '2025-09-05T19:02:14.000Z', 'id': '1964041398333637090', 'edit_history_tweet_ids': ['1964041398333637090']}, {'public_metrics': {'retweet_count': 3, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 0}, 'text': 'RT @bigtimeLuca: Is #CashAppFriday back for real? Bet \n\nLike &amp; Drop your CashApp\n\nI’m blessing a few active followers ✅', 'author_id': '1257222162999623682', 'created_at': '2025-09-05T19:02:12.000Z', 'id': '1964041390800711734', 'edit_history_tweet_ids': ['1964041390800711734']}, {'public_metrics': {'retweet_count': 0, 'reply_count': 1, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 0}, 'text': "C'mon #CashAppFriday", 'author_id': '1377316200095551496', 'created_at': '2025-09-05T19:02:11.000Z', 'id': '1964041387709489295', 'edit_history_tweet_ids': ['1964041387709489295']}, {'public_metrics': {'retweet_count': 0, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 2}, 'text': '@CashApp #CashAppFriday $ckgthedonchi https://t.co/ZAMStkueVb https://t.co/Tgt5QPGKIp', 'author_id': '1692268994487881728', 'created_at': '2025-09-05T19:02:11.000Z', 'id': '1964041387693011315', 'edit_history_tweet_ids': ['1964041387693011315']}, {'public_metrics': {'retweet_count': 0, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 0}, 'text': '@CashApp  #CashAppFriday \nI owe y’all like $100 help me out here $Joyn3r90 https://t.co/cYnFLEDa0L', 'author_id': '796170088617480192', 'created_at': '2025-09-05T19:02:07.000Z', 'id': '1964041372228333885', 'edit_history_tweet_ids': ['1964041372228333885']}, {'public_metrics': {'retweet_count': 0, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 0}, 'text': "@CashApp It's Friiiiidaaaaayyyyy! Time to play!  \n💚👀\n#CashAppFriday", 'author_id': '959131658640330752', 'created_at': '2025-09-05T19:01:59.000Z', 'id': '1964041337952403884', 'edit_history_tweet_ids': ['1964041337952403884']}, {'public_metrics': {'retweet_count': 3, 'reply_count': 7, 'like_count': 12, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 21}, 'text': 'Is #CashAppFriday back for real? Bet \n\nLike &amp; Drop your CashApp\n\nI’m blessing a few active followers ✅', 'author_id': '1337096562749677575', 'created_at': '2025-09-05T19:01:59.000Z', 'id': '1964041336803168443', 'edit_history_tweet_ids': ['1964041336803168443']}, {'public_metrics': {'retweet_count': 0, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 2}, 'text': '@CashApp #CashAppFriday', 'author_id': '1352199789530783746', 'created_at': '2025-09-05T19:01:50.000Z', 'id': '1964041301235470478', 'edit_history_tweet_ids': ['1964041301235470478']}, {'public_metrics': {'retweet_count': 0, 'reply_count': 2, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 2}, 'text': '@CashApp I heard yall was being nice to folks on a Good Friday 👀  #CashAppFriday $Preme150', 'author_id': '46560708', 'created_at': '2025-09-05T19:01:44.000Z', 'id': '1964041274018746452', 'edit_history_tweet_ids': ['1964041274018746452']}, {'public_metrics': {'retweet_count': 0, 'reply_count': 1, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 3}, 'text': '@CashApp I too would like to feel seen.. LOL\n\n#CashAppFriday\n\n$TheKidFromBrooklyn', 'author_id': '297945249', 'created_at': '2025-09-05T19:01:34.000Z', 'id': '1964041231039619415', 'edit_history_tweet_ids': ['1964041231039619415']}]

    # return data


