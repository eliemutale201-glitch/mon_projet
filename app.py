print("Bienvenue dans le gestionnaire d'utilisateurs 👥")

utilisateurs = []

def ajouter_utilisateur():
    nom = input("Nom : ")
    age = int(input("Âge : "))

    utilisateur = {
        "nom": nom,
        "age": age
    }

    utilisateurs.append(utilisateur)
    print("Utilisateur ajouté ✅")

def afficher_utilisateurs():
    if not utilisateurs:
        print("Aucun utilisateur ❌")
        return
    
    for user in utilisateurs:
        print(f"Nom : {user['nom']} | Âge : {user['age']}")

def menu():
    while True:
        print("\n1. Ajouter utilisateur")
        print("2. Afficher utilisateurs")
        print("3. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            ajouter_utilisateur()
        elif choix == "2":
            afficher_utilisateurs()
        elif choix == "3":
            break
        else:
            print("Choix invalide ❌")

menu()