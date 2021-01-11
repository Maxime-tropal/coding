noms = ["Estelle DURAND", "Jean DUJARDIN"]
codes = ["10201413","12457424"]

input_nom = str(input("Entrez le prénom et nom : "))

while True:
    if input_nom in noms:
        input_mdp = str(input(f"Entrez le code associé à {input_nom} : "))
        if input_mdp in codes:
            print(f"Bienvenue {input_nom}!")
            break
        else:
            print("Code erroné !")
            continue
    else:
        input_nom = str(input("Entrez un prénon/nom valide : "))