# Start Here

## Structure

The backend is divided into three parts.
```
└───backend
    └───app <-- Our main Backend App (Fast API)
      ├───songs <-- routes for our Song matching API
      ├───genius <-- Objects and tests for Genius API
      └───twitter <-- Objects and tests for Twitter API
```
`genius` and `twitter` are called within `songs`.

### app - Fast API
Our main app uses the Fast API Python Web Framework
Info [here](https://docs.tweetbrain.tisuela.com/backend/fastapi/)

## songs - Fast API
This portion of the application holds all our routes for our Song API endpoints.

Our objects from `genius` and `twitter` are used within `songs` to return songs which match a user's timeline (timeline = list of tweets).

### genius - lyricgenius

We are using a Python wrapper for Genius's API called `lyricgenius`

[🧠 find out more about `lyricgenius`](https://lyricsgenius.readthedocs.io/en/master/)

### twitter - tweepy

We are using a Python wrapper for Twitter's API called `tweepy`

[🧠 find out more about `tweepy`](http://docs.tweepy.org/en/latest/)

In addition to that, we are using `nltk` to process the tweets and figure out the most common words from a user's timeline.


## Quick Start
Below are the instructions for running Fast API locally

### Installation
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

You should find yourself here:
```
└───tweetbrain
    └───backend <-- you are here
```

**🐍 Create Python virtual environment**

There are a good amount of depencies for this project -- it will be good practice to use a virtual environment, albeit not necessary.

=== "macOS/Linux"

  ```
  python3 -m venv env
  ```

=== "Windows Command Line"

  ```
  python -m venv env
  ```

=== "Windows Powershell"

  ```
  python -m venv env
  ```

The last argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.


**✅ Activate virtual environment**

=== "macOS/Linux"
  ```
  source env/bin/activate
  ```
=== "Windows Command Line"

  ```
  .\env\Scripts\activate.bat
  ```
=== "Windows Powershell"
  ```
  .\env\Scripts\activate.ps1
  ```


**📦 Navigate to the repository folder and install packages**

```
python -m pip install -r requirements.txt
```


### Configuration
**🔐 This portion provides authentication information, which is NOT in our repository**

#### Method 1: secrets.json

💾 Those who are a part of our Web Jam team have access to a `secrets.json` file. This is the simplest way -- even if you don't have this file, you can make your own with the same name.
Download that file, and paste it within `tweetbrain/backend`:
```
└───tweetbrain
    └───backend <-- paste secrets.json within here
        └───secrets.json
```

### Method 2: Set environmental variables

🌳 If you do not have our json file, or if you cannot use it for some reason, you will need to write environmental variables within your terminal. **These variables must be made in the terminal/shell where your virtual environment is running**

The environmental variables are specified within [`tweetbrain/backend/config.py`](https://github.com/tweetbrain/you/blob/main/tweetbrain/backend/app/config.py).

To set environmental variables, follow these instructions:


!!! Twitter API Tokens/Secrets
=== "macOS/Linux"
  ``` bash
  export CONSUMER_KEY=your_consumer_key
  export CONSUMER_SECRET=your_consumer_secret
  export ACCESS_TOKEN=your_access_token
  export ACCESS_SECRET=your_access_secret
  ```
=== "Windows Command Line"
  ``` bat
  set CONSUMER_KEY=your_consumer_key
  set CONSUMER_SECRET=your_consumer_secret
  set ACCESS_TOKEN=your_access_token
  set ACCESS_SECRET=your_access_secret
  ```
=== "Windows Powershell"
  ``` powershell
  $env:CONSUMER_KEY="your_consumer_key"
  $env:CONSUMER_SECRET="your_consumer_secret"
  $env:ACCESS_TOKEN="your_access_token"
  $env:ACCESS_SECRET="your_access_secret"
  ```

**Genius API Tokens**

=== "macOS/Linux"
  ```
  export GENIUS_ACCESS_TOKEN=your_genius_access_token
  ```
=== "Windows Command Line"
  ```
  set GENIUS_ACCESS_TOKEN=your_genius_access_token
  ```
=== "Windows Powershell"
  ```
  $env:GENIUS_ACCESS_TOKEN="your_genius_access_token"
  ```


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
