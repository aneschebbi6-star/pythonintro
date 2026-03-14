
import os

def lire_csv(nom_fichier):
    etudiants = []
    if not os.path.exists(nom_fichier):
        print(f"Erreur : Le fichier '{nom_fichier}' est introuvable.")
        return etudiants
        
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            if not lignes:
                return etudiants
                
            entetes = lignes[0].strip().split(",")
            for ligne in lignes[1:]:
                valeurs = ligne.strip().split(",")
                if len(valeurs) < 2:
                    continue
                nom, note = valeurs[0], valeurs[1]
                etudiant = {
                    "nom": nom,
                    "note": note
                }
                etudiants.append(etudiant)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        
    return etudiants


def calculer_moyenne(etudiants):
    if not etudiants:
        return 0
    total = 0
    count = 0
    for etudiant in etudiants:
        try:
            total += float(etudiant["note"])
            count += 1
        except ValueError:
            print(f"Avertissement : Note invalide pour {etudiant['nom']}")
            
    return total / count if count > 0 else 0


def afficher_resultats(etudiants, moyenne):
    continuer = True
    while continuer:
        print("\n--- Menu Extraction CSV ---")
        print("1. Affichage des étudiants")
        print("2. Nombre d'étudiants")
        print("3. Note moyenne de la classe")
        print("4. Quitter")
        
        choix = input("Votre choix : ").strip()

        if choix == "1":
            if not etudiants:
                print("Aucun étudiant trouvé.")
            else:
                for e in etudiants:
                    print(f"{e['nom']} a eu {e['note']}")
        elif choix == "2":
            print(f"Le nombre total d'étudiants est {len(etudiants)}")
        elif choix == "3":
            print(f"La moyenne de la classe est {moyenne:.2f}")
        elif choix == "4":
            print("Au revoir !")
            continuer = False
        else:
            print("Option invalide, veuillez réessayer.")


# --- Programme principal ---
if __name__ == "__main__":
    # Résoudre le chemin absolu du fichier CSV par rapport au script
    dossier_script = os.path.dirname(os.path.abspath(__file__))
    nom_csv = os.path.join(dossier_script, "notes.csv")
    
    liste_etudiants = lire_csv(nom_csv)
    if liste_etudiants:
        moy_classe = calculer_moyenne(liste_etudiants)
        afficher_resultats(liste_etudiants, moy_classe)
    else:
        print("Impossible de charger les données.")
