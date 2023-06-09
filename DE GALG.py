from time import sleep
from random import choice

def listmaker(filename, splitter):#om bestanden te openen en lists te maken er van
    file = open(filename, "r", encoding="utf8")
    a = file.read().split(splitter)
    file.close()
    return a

woord = choice(listmaker(input("welke lijst?\n"), "\n")).casefold()#woordenlijst van https://opentaal.org
galg = listmaker("galg.txt", ",")#plaatjes zelf gemaakt
text = choice(listmaker("galg logo.txt", "/,/"))#leuke logo's zijn van https://patorjk.com/software/taag

antwoord = ""#alle variables definen
fouten = 0
goedgegokt = ""
foutgegokt = ""

print("\n"*100+"Welkom bij\n\n"+text)#logo printen
sleep(3)

game = True
while game:
    #calculate 
    if len(antwoord) < 2 and antwoord in woord:#een correcte letter
        goedgegokt += antwoord
        print_woord = ""
        for i in woord:#gaat door elke letter in hte woord en kijkt of je die gegokthebt of dat het een spatie is
            if i in goedgegokt:
                print_woord += i
            elif i == " ":
                print_woord += " "
            else:
                print_woord += "-"
    
    elif antwoord == woord:#correct woord = gewonnen
        win = True
        game = False
    
    elif antwoord != "QQ":#fout
        foutgegokt += antwoord + ", "
        fouten += 1
    
    if fouten == 10 or antwoord == "QQ":
        win = False
        game = False
    #print/vraag
    print("\n"*100+galg[fouten])#ja hoor, bijna alles in één lijn, jalloers hè
    antwoord=input("\nhet woord is:\n"+print_woord+"\n\nje hebt nog "+str(10-fouten)+" pogingen over,\n\ndit heb je al geraden:\n"+foutgegokt+"\n\nraadt het woord of een letter of type QQ om te stoppen\n") if game else print("\ngoed gedaan, het woord was inderdaad \""+woord+"\"! je hebt gewonnen!") if win else print("\n\njammer, het woord was \""+woord+"\". je hebt verloren, volgende keer beter")
sleep(5)