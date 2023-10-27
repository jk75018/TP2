import random

word_list = ["chien", "chat", "maison", "soleil", "ordinateur", "pizza", "fleur", "plage", "montagne", "arc-en-ciel"]

def generate_random_passphrase(num_words):
    # Génération d'une passphrase aléatoire en choisissant des mots de manière aléatoire dans notre liste
    passphrase = [random.choice(word_list) for _ in range(num_words)]
    return ' '.join(passphrase)
