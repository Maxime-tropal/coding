benef_de_la_semaine = 31000000
nb_semaine = 1
benef_total = 0


while benef_total<150000000:
    benef_total = benef_total + benef_de_la_semaine
    benef_de_la_semaine = benef_de_la_semaine*(80/100)
    nb_semaine = nb_semaine+1
print(nb_semaine, benef_total)