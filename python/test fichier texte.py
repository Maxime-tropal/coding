text = open("C:\\Users\\maxem\\Desktop\\e_20111031.txt", "r").readlines()

count = 0

with open ("C:\\Users\\maxem\\Desktop\\test.txt", "w") as f:
    for lines in text[0].split():
        for word in lines.split(';'):
            if word == "BO":
                count += 1
            print(count)
            #liste1 = [word]
            #f.write(str(liste1))

print(count)