

Bans=("Hakcer1","tocxix","Diego123")
rawLogins = ["ray","maria","ray","tocxix","Eather","Diego123"]
Clean = {""}
NUMBER = 0
aprovedplayers = [""]


for x in rawLogins:
    adding = x
    Clean.add(adding)

Clean.remove("")

for x in Clean:

    adding = x

    if x not in Bans:
     aprovedplayers.append(x)



aprovedplayers.remove("")
print(aprovedplayers)

