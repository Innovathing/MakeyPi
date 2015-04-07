
import random

hashtags = " #iot #insa #LaBonneMangeoire"
messages = [
			"Oh le bel oiseau !",
			"Laisses-en pour les autres !",
			"Piou piou piou"]

def get_message():
	ret = random.choice(messages) + hashtags
	return ret[:140]
