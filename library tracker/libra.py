from pickle import load, dump

biblio = []

print("Choisissez le type de fichier pour stocker les livres :")
print("1. Texte")
print("2. Binaire")
chois = input("choisir le type de fichier : ")

# Chargement des données
if chois == "1":
    try:
        f = open("biblio.txt", "r")
        for line in f:
            champs = line.strip().split(";")
            if len(champs) == 4:
                titre, auteur, annee, categorie = champs
                livre = {
                    "titre": titre,
                    "auteur": auteur,
                    "annee": annee,
                    "categorie": categorie
                }
                biblio.append(livre)
        f.close()
    except FileNotFoundError:
        print("Erreur: Le fichier biblio.txt est introuvable.")

elif chois == "2":
    try:
        ff = open("biblio.dat", "rb")
        biblio = load(ff)
        ff.close()
    except FileNotFoundError:
        print("Erreur: Le fichier biblio.dat est introuvable.")
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")

def sauvegarder():
    if chois == "1":
        f = open("biblio.txt", "w")
        for livre in biblio:
            f.write(f"{livre['titre']};{livre['auteur']};{livre['annee']};{livre['categorie']}\n")
        f.close()
    elif chois == "2":
        ff = open("biblio.dat", "wb")
        dump(biblio, ff)
        ff.close()

ok = True
while ok:
    print("\n1; Ajouter un livre")
    print("2; Voir tous les livres")
    print("3; Nombre total de livres")
    print("4; Total par catégorie")
    print("5; Rechercher par titre ou auteur")
    print("6; Modifier un livre")
    print("7; Supprimer un livre")
    print("8; Quitter")

    choix = input("Choisir une option : ")

    if choix == "1":
        titre = input("Entrer le titre du livre : ")
        auteur = input("Auteur : ")
        categorie = input("Categorie : ")
        annee = input("Année de publication : ")
        biblio.append({"titre": titre, "auteur": auteur, "categorie": categorie, "annee": annee})
        sauvegarder()
        print("Livre ajouté et sauvegardé")

    elif choix == "2":
        if len(biblio) == 0:
            print("Aucun livre dans la bibliothèque.")
        else:
            print(f"\n{'Titre':<20} {'Auteur':<20} {'Catégorie':<15} {'Année':<5}")
            print("-" * 65)
            for livre in biblio:
                print(f"{livre['titre']:<20} {livre['auteur']:<20} {livre['categorie']:<15} {livre['annee']:<5}")

    elif choix == "3":
        print("Nombre total de livres :", len(biblio))

    elif choix == "4":
        categ_u = []
        for livre in biblio:
            if livre["categorie"] not in categ_u:
                categ_u.append(livre["categorie"])
        
        for c in categ_u:
            count = 0
            for livre in biblio:
                if livre["categorie"] == c:
                    count += 1
            print(f"{c} : {count}")

    elif choix == "5":
        rech = input("Entrer titre ou auteur à rechercher : ").lower()
        trouve = False
        for livre in biblio:
            if rech in livre["titre"].lower() or rech in livre["auteur"].lower():
                print(f"Trouvé: {livre['titre']} - {livre['auteur']} ({livre['categorie']}, {livre['annee']})")
                trouve = True
        if not trouve:
            print("Aucun résultat trouvé.")

    elif choix == "6":
        titre_mod = input("Entrer le titre du livre à modifier : ")
        trouve = False
        for livre in biblio:
            if livre["titre"].lower() == titre_mod.lower():
                print("Livre trouvé. Laissez vide pour ne pas modifier un champ.")
                nouvel_auteur = input(f"Nouvel auteur [{livre['auteur']}] : ")
                nouvelle_cat = input(f"Nouvelle catégorie [{livre['categorie']}] : ")
                nouvelle_annee = input(f"Nouvelle année [{livre['annee']}] : ")
                
                if nouvel_auteur: livre["auteur"] = nouvel_auteur
                if nouvelle_cat: livre["categorie"] = nouvelle_cat
                if nouvelle_annee: livre["annee"] = nouvelle_annee
                
                sauvegarder()
                print("Livre modifié et sauvegardé.")
                trouve = True
                break
        if not trouve:
            print("Livre non trouvé.")

    elif choix == "7":
        titre_sup = input("Entrer le titre du livre à supprimer : ")
        trouve = False
        for i in range(len(biblio)):
            if biblio[i]["titre"].lower() == titre_sup.lower():
                del biblio[i]
                sauvegarder()
                print("Livre supprimé et sauvegardé.")
                trouve = True
                break
        if not trouve:
            print("Livre non trouvé.")

    elif choix == "8":
        print("Au revoir !")
        ok = False
    else:
        print("Option invalide.")
