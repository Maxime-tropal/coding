villes = ["Paris", "Lyon", "Marseille", "Bordeaux", "Nice"]
distances = [[], [350], [800,300], [900,600,500], [1000,600,250,1200]]
numero_ville = 0
for ville in villes:
    i=0
    for distance in distances[numero_ville]:
        print("Distance ", ville, " - ", villes[i], " : ", distance, " km")
        i=i+1
    numero_ville = numero_ville+1