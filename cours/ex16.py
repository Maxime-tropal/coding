mdp = str(input("Entrez votre mot de passe : "))
confirmation_mdp = str(input("Confirmez votre mot de passe : "))
while confirmation_mdp != mdp:
    confirmation_mdp = str(input("Confirmez votre mot de passe : "))

print("Connexion reussie")
