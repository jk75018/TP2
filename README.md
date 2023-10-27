# Projet 2 : Gestionnaire de Sécurité

# Ce script en Python constitue un outil de sécurité polyvalent offrant diverses fonctionnalités liées à la gestion des mots de passe. Il comporte un générateur de mots de passe, un évaluateur de la robustesse des mots de passe et un générateur de phrases confidentielles. Les fonctionnalités sont détaillées ci-dessous :

# Menu

# Lorsque vous lancez le programme, vous serez accueilli par un menu présentant les options suivantes :

menu = """
Menu :
1. Génération de Mot de Passe
2. Évaluation de la Robustesse du Mot de Passe
3. Génération de Phrase Confidentielle
4. Retour au Menu Principal
5. Quitter
"""

# Vous pouvez sélectionner une option en entrant le numéro correspondant.

# 1. Génération de Mot de Passe

# Cette fonctionnalité vous permet de générer un mot de passe aléatoire en fonction des critères que vous spécifiez. Vous pouvez définir la longueur du mot de passe ainsi que le nombre de lettres minuscules, de lettres majuscules, de chiffres et de caractères spéciaux dans le mot de passe.

# 2. Évaluation de la Robustesse du Mot de Passe

# L'évaluateur de mots de passe vérifie la solidité d'un mot de passe en fonction de son entropie. Il vous indique si le mot de passe est classé comme "Très faible", "Faible", "Moyen" ou "Fort" en fonction de l'entropie calculée.

# 3. Génération de Phrase Confidentielle

# Cette fonction génère une phrase confidentielle basée sur une liste de mots prédéfinis. Vous pouvez spécifier le nombre de mots dans la phrase confidentielle.

# Utilisation du Programme

# Pour utiliser le programme :

# Assurez-vous d'avoir Python installé sur votre système.

# Exécutez le script principal.
def main():
    while True:
        print(menu)
        choix = input("Sélectionnez une option : ")
        if choix == "1":
            generer_mot_de_passe()
        elif choix == "2":
            evaluer_robustesse_mot_de_passe()
        elif choix == "3":
            generer_phrase_confidentielle()
        elif choix == "4":
            continue
        elif choix == "5":
            print("Programme terminé.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

# Définition des fonctions pour chaque option du menu

def generer_mot_de_passe():
    # Implémenter la génération de mot de passe ici
    pass

def evaluer_robustesse_mot_de_passe():
    # Implémenter l'évaluation de la robustesse du mot de passe ici
    pass

def generer_phrase_confidentielle():
    # Implémenter la génération de phrase confidentielle ici
    pass

if __name__ == "__main__":
    main()