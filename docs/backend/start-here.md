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

In addition to that, we are using `nltk` to process the tweets and figure out the most common words from a user's timeline.


## Quick Start
Below are the instructions for running Fast API locally


**👩‍👧 Clone repository**
```
git clone https://github.com/tweetbrain/you
cd you
```

Navigate to `tweetbrain/backend`
```
cd tweetbrain
cd backend
```

**🐍 Create Python virtual environment**

There are a good amount of depencies for this project -- it will be good practice to use a virtual environment, albeit not necessary.

On macOS and Linux:
`python3 -m virtualenv env`

On Windows:
`python -m venv env`
The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.


**✅ Activate virtual environment**

On macOS and Linux:
`source env/bin/activate`

On Windows Command Line:
`.\env\Scripts\activate.bat`

One Windows Powershell
`.\env\Scripts\activate.ps1`

**📦 Navigate to the repository folder and install packages**

`python -m pip install -r requirements.txt`


**🦄 Run Fast API using uvicorn**

Run uvicorn.
```
uvicorn app.main:app --reload
```

You’ll see output similar to this:

```
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
←[32mINFO←[0m:     Started reloader process [←[36m←[1m38240←[0m] using ←[36m←[1mstatreload←[0m
←[32mINFO←[0m:     Started server process [←[36m13020←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
```
donezo
