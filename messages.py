#encoding: utf-8

import random

hashtags = " #iot #insa #LaBonneMangeoire"
messages = [
			"Oh le bel oiseau !",
			"Laisses-en pour les autres !",
			"Piou piou piou",
			"Mais laissez moi manger enfin !",
			"Certes je suis un oiseau, mais j'ai tout de même le droit à un peu d'intimité.",
			"Je prendrai le plat du jour",
			"Serveur ? Il y avait un insecte dans mon plat !",
			"La vie privée ça ne vous dit rien ?",
			"Maxi Bestof Bigmac, frites eeeet coca please.",
			"A trois je me tire sans payer, un ... deux ...",
			"Say hello to my little friend",
			"Tu ne dois pas connaître Hitchcock toi ?",
			"Le bonheur n’est réel que lorsqu’il est dans ma bouche.",
			"Selfiiiie",
			"C'est un fléau pour la selection naturelle; mais c'est bon. !",
			"Ceci n'est pas un oiseau",
			"Wesh ça va ?",
			"Elle est un peu à l'arrache cette mangeoire non ?",
			"Don't kill the eating bird",
			"Birdy miam miam"]

def get_message():
	ret = random.choice(messages) + hashtags
	return ret[:140]
