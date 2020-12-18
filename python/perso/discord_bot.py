import discord, os, requests, json, random

Token = "Nzg5MjIwMTEwNjU2OTk1MzI4.X9u4gQ.sgog4GWfoxesk7VtIEVG51A8JoU" #mot de passe du bot
client = discord.Client() #indique qu'on utilise le client discord

words = ["post", "eussou", "boucle", "forum", "terraria"]

starter_encouragements = ["t mort", "EUSSSOUUUUU", "AGNEUGNEU", "The eye of Cthulu has awoken"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random") # on interroge l'api zenquotes qui nous retourne une citation en format json
    json_data = json.loads(response.text)
    citation = json_data[0]['q'] + " -" + json_data[0]['a'] # q est une clé qui contient la citation, a = auteur
    return(citation)

#chaque action est définie par un event, le nom des fonctions correspond a des fonctions prédéfinies dans le module discord.

@client.event
async def on_ready(): #fonction qui se lance quand le bot démarre.
    print("Connecté en tant que {0.user}".format(client))

@client.event
async def on_message(message): #se lance dès qu'un message est reçu sauf en excluant ses propres messages
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith("!post"): # on définit la commande pour intéragir avec le bot ici "!"
        citation = get_quote()
        await message.channel.send(citation) #envoie un message dans le channel correspondant

    if any(word in msg for word in words):
        await message.channel.send(random.choice(starter_encouragements))

client.run(Token)