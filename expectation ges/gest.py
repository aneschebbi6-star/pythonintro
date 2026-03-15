def lire_fichier(nom_fichier):
    try:
        f=open(nom_fichier,"r")
        ch=f.read()
        print(ch)
        f.close()


    except FileNotFoundError:
        print("erreur: fichier introuvable")
    else:
        print("fichier lue avec succes")
    finally:
        print("tentative terminee")


def diviser(a, b):
    try:
        res=a/b
        print(res)
    except ZeroDivisionError:
        print("erreur:1")
    else:
        print(f"resultat:{res} terminee")
    finally:
        print("finallement reussis")

def convertir_note(valeur):
    try:
        return int(valeur)
    except ValueError:
        print("erreur 1: valeur invalide")
    finally:
        print("conversion terminee")


# --- Tests ---
lire_fichier("fichier_qui_nexiste_pas.txt")
lire_fichier("notes.csv")

diviser(10, 2)
diviser(10, 0)

convertir_note("18")
convertir_note("abc")