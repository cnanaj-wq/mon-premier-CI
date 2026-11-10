def verifier_nom(nom):
    if nom is None or nom.strip() == "":
        raise ValueError("Le nom est obligatoire")

    return True