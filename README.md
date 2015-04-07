# MakeyPi
A connected Bird table to take a picture every time it lands

## Config && Install

MakeyPi needs some python libraries : evdev, tweepy
```
# pip install evdev tweepy
```

If you have an error like ```Python.h blablabla```. Just install ```python-dev``` package :
```
# apt-get install python-dev
```

You should also create a file ```config.py``` with your twitter API keys :
```python
CONSUMER_KEY = "XXXX"
CONSUMER_SECRET = "XXXX"
ACCESS_TOKEN = "XXXX"
ACCESS_TOKEN_SECRET = "XXXX"
```

## Install daemon

```bash
# cp makeypi /etc/init.d/makeypi
```

## Run daemon

```bash
# service makeypi start
```

## Add daemon at startup

```bash
# insserv makeypi
```

## Remove ademon at startup

```bash
# insserv -r makeypi
```