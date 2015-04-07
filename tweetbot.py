
import tweepy
from config import *

def connect_api():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	return api

def update_status_pix(text, image):
	api.update_with_media(filename=image, status=text)
