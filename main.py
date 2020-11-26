import random
#words = ["hazbin", "meme", "yacoding", "doge", "red"]
words = []
wronged = []
with open("words.txt") as f:
    for line in f:
        words.append(line.strip())
def gameloop(arrin):
    wronged = []
    currdisplay = ""
    guessword = words[arrin].lower()
    lives = 5
    for element in range(0, len(guessword)):
        if guessword[element] != " ":
            currdisplay = currdisplay + "_"
        else:
            currdisplay = currdisplay + " "
    while True:
        ifCorr = ""
        print("Current wrong letters: ", wronged)
        print("Lives: " + str(lives) + "\n" + currdisplay)        
        imp = input("Guess a letter: ").lower()
        for element in range(0, len(guessword)):
            if guessword[element] == imp:
                currlist = list(currdisplay)
                currlist[element] = imp
                currdisplay = "".join(currlist)
                ifCorr = True
        if guessword == currdisplay:
            print(currdisplay, "\nWinner!")
            while True:
                imp = input("Play again (Y/N)? ")
                if imp.lower() == "y":
                    print("Playing again!")
                    main()
                elif imp.lower() == "n":
                    print("Thanks for playing!")
                    exit()
                else:
                    print("Not a command.")
        if ifCorr != True:
            lives = lives - 1
            wronged.append(imp)
        if lives <= 0:
            print("You lost lol", "\nThe word was:", guessword)
            while True:
                imp = input("Play again (Y/N)? ")
                if imp.lower() == "y":
                    print("Playing again!")
                    main()
                elif imp.lower() == "n":
                    print("Thanks for playing!")
                    exit()
                else:
                    print("Not a command.")
def main():
    gameloop(random.randrange(0, len(words)))
main()
