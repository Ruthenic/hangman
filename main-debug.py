import random
#words = ["hazbin", "meme", "yacoding", "doge", "red"]
words = []
with open("words.txt") as f:
    for line in f:
        print("Debug (reading line from file to list): " + line)
        words.append(line.strip())
print("Debug (word list): ")
print(words)
def gameloop(arrin):
    currdisplay = ""
    guessword = words[arrin].lower()
    lives = 5
    for element in range(0, len(guessword)):
        print("Debug(elements while checking for spaces): " + str(element))
        if guessword[element] != " ":
            currdisplay = currdisplay + "_"
        else:
            currdisplay = currdisplay + "-"
        print("Debug (current displayed): " + currdisplay)
    while True:
        ifCorr = ""
        print("Debug (current word to guess): " + guessword)
        print("Lives: " + str(lives))
        print(currdisplay)
        imp = input("Guess a letter: ").lower()
        for element in range(0, len(guessword)):
            if guessword[element] == imp:
                currlist = list(currdisplay)
                currlist[element] = imp
                currdisplay = "".join(currlist)
                ifCorr = True
        if guessword == currdisplay:
            print(currdisplay)
            print("Winner!")
            exit()
        if ifCorr != True:
            lives = lives - 1
        if lives == 0:
            print("You lost lol")
            exit()

while True:
    gameloop(random.randrange(0, len(words)))
