dep = []
cat = []

# Charger les dépenses existantes
ok = True
try:
    f = open("expences.txt", "r")
    for line in f:
        montant, categorie = line.strip().split(";")
        dep.append(float(montant))
        cat.append(categorie)
    f.close()
except FileNotFoundError:
    pass  # fichier pas encore créé

# Boucle principale
while ok:

    print("\n1; ajouter depense")
    print("2; voir depenses")
    print("3; voir total")
    print("4; total par categorie")
    print("5; quitter")

    choix = input("Choisir une option : ")

    if choix == "1":
        montant = float(input("Entrer montant : "))
        categorie = input("Entrer categorie : ")

        dep.append(montant)
        cat.append(categorie)

        # sauvegarder dans le fichier
        f = open("expences.txt", "a")
        f.write(f"{montant};{categorie}\n")
        f.close()

        print("Depense ajoutee et sauvegardee")

    elif choix == "2":
        if len(dep) == 0:
            print("Aucune depense")
        else:
            for i in range(len(dep)):
                print(dep[i], "-", cat[i])
            print("Nombre de depenses :", len(dep))

    elif choix == "3":
        t = 0
        for i in range(len(dep)):
            t += dep[i]
        print("Total :", t)

    elif choix == "4":
        categories_uniques = []
        for i in range(len(cat)):
            if cat[i] not in categories_uniques:
                categories_uniques.append(cat[i])

        for j in range(len(categories_uniques)):
            total_cat = 0
            for i in range(len(cat)):
                if cat[i] == categories_uniques[j]:
                    total_cat += dep[i]
            print(categories_uniques[j], ":", total_cat)

    elif choix == "5":
        print("Quitter")
        ok = False