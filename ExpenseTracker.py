from numpy import array


def tracker():
    dep = []
    cat = []

    while True:
        print("\n1; ajouter depense")
        print("2; voir depenses")
        print("3; voir total")
        print("4; voir nombre depenses")

        print("5; quitter")

        choix = input("Choisir une option : ")

        if choix == "1":

            montant = float(input("Entrer montant : "))
            categorie = input("Entrer categorie : ")

            dep.append(montant)
            cat.append(categorie)

            print("Depense ajoutee")

        elif choix == "2":

            for i in range(len(dep)):
                print(dep[i], "-", cat[i])

        elif choix == "3":

            t = 0
            for i in range(len(dep)):
                t += dep[i]
            print("Total :", t)

        elif choix == "4":
            l = len(dep)
            print("LE totale de depenseset ", l)

        elif choix == "5":
            print("Quitter")
            return False


tracker()
