class NoteInvalide(Exception):
    def __init__(self, note):
        self.note = note
        super().__init__(f"{note} est hors de [0, 20]")

class NomInvalide(Exception):
    def __init__(self, nom):
        self.nom = nom
        super().__init__(f"'{nom}' est un nom invalide")
    




def valider_note(note):
    if note < 0 or note > 20:
        raise NoteInvalide(note)  # ici on la lance
    return note


def valider_nom(nom):
    if not nom or any(c.isdigit() for c in nom):
        raise NomInvalide(nom)
    return nom
  

def ajouter_etudiant(nom, note):
    try:
        valider_nom(nom)
        valider_note(note)
        print("etudiant ajoutee")
    except NomInvalide as e:
        print(e)
    except NoteInvalide as e:
        print(e)

        


# --- Tests ---
ajouter_etudiant("Anes", 18)     # ✅ valide
ajouter_etudiant("Ali", 25)      # ❌ note invalide
ajouter_etudiant("", 15)         # ❌ nom vide
ajouter_etudiant("An3s", 14)    # ❌ nom avec chiffre