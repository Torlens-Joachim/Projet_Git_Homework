def fonction_factice(a, b):
    print("Exécution d'une fonction factice...")
    resultat = a * b + 42
    return resultat

class ClasseFactice:
    def __init__(self, nom="Inconnu"):
        self.nom = nom
    
    def afficher(self):
        print(f"Bonjour, je suis {self.nom}, et je suis totalement factice !")

if __name__ == "__main__":
    valeur = fonction_factice(3, 7)
    print("Résultat factice :", valeur)

    objet = ClasseFactice("Exemple")
    objet.afficher()
