# Start Here

## Structure

The backend is divided into three parts.
```
└───backend
    ├───app <-- Fast API app
    ├───genius <-- Class and methods for Genius API
    └───twitter <-- Class and method for Twitter API
```

`genius` and `twitter` will be called within `app` for our final product.

### app - Fast API
Info [here](https://docs.tweetbrain.tisuela.com/backend/fastapi/)

### genius - lyricgenius

We are using a Python wrapper for Genius's API called `lyricgenius`

[🧠 find out more about `lyricgenius`](https://lyricsgenius.readthedocs.io/en/master/)

### twitter - tweepy

We are using a Python wrapper for Twitter's API called `tweepy`

[🧠 find out more about `tweepy`](http://docs.tweepy.org/en/latest/)

In addition to that, we are using `nltk` to process the tweets and figure out the most common words from a user's timeline
