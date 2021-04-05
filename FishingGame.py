import random

random.seed()   #Prepare random number generator

value = 0
score = 0
total = 0
print("Welcome to the Fishing Game! Would you like to head out to fish or stay on shore?")
print("1. Go Fish!")
print("2. Stay on shore!")
choice = int(input())
while choice < 1 or choice > 2:
    print("Invalid input! Would you like to head out to fish or stay on shore? (1 or 2)")
    print("1. Go Fish!")
    print("2. Stay on shore!")
    choice = int(input())
if choice == 1:
    while True:    #This simulates a Do Loop
        rustyCan = 0
        tinyFish = 0
        smallFish = 0
        mediumFish = 0
        largeFish = 0
        hugeFish = 0
        while True:    #This simulates a Do Loop
            print("Fishing...")
            value = int(random.random() * 100) + 1
            if value <= 40:
                print("You caught a rusty can +10 points!")
                score = 10
                rustyCan = rustyCan + 1
            else:
                if value <= 60:
                    print("You caught a tiny fish +20 points!")
                    score = 20
                    tinyFish = tinyFish + 1
                else:
                    if value <= 80:
                        print("You caught a small fish +30 points!")
                        score = 30
                        smallFish = smallFish + 1
                    else:
                        if value <= 90:
                            print("You caught a medium fish +60 points!")
                            score = 60
                            mediumFish = mediumFish + 1
                        else:
                            if value <= 98:
                                print("You caught a large fish! +80 points!")
                                score = 80
                                largeFish = largeFish + 1
                            else:
                                print("You caught a huge fish +100 points!")
                                score = 100
                                hugeFish = hugeFish + 1
            total = total + score
            print("Would you like to continue fishing? (Y/N)")
            keepFishing = input()
            while keepFishing != "Y" and keepFishing != "y" and keepFishing != "N" and keepFishing != "n":
                print("Please enter (Y/N). Would you like to keep fishing? (Y/N)")
                keepFishing = input()
            if not(keepFishing == "Y" or keepFishing == "y"): break   #Exit loop
        print("Total score: " + str(total))
        print("You caught: " + str(rustyCan) + " rusty cans, " + str(tinyFish) + " tiny fish, " + str(smallFish) + " small fish, " + str(mediumFish) + " medium fish, " + str(largeFish) + " large fish, and " + str(hugeFish) + " huge fish.")
        if total <= 200:
            print("Better luck next time")
        else:
            if total <= 300:
                print("Good job")
            else:
                if total <= 999:
                    print("You fished well")
                else:
                    print("You are the fishing champion!")
        print("Would you like play again? (Y/N)")
        keepPlaying = input()
        while keepPlaying != "Y" and keepPlaying != "y" and keepPlaying != "N" and keepPlaying != "n":
            print("Invalid input! Please enter (Y/N). Would you like play again? (Y/N)")
            keepPlaying = input()
        if not(keepPlaying == "Y" or keepPlaying == "y"): break   #Exit loop
print("You have chosen to stop fishing! Goodbye!")
