#Name: Leon Chen
#Date: June 2
#This program lets the user answer one word, true/false, or multiple choice questions and prints the statistics of the answers. It is also possible to loop the program multiple times.
import random

#initializing all the variables and introduction
print("This quiz is on anything related to animals or the environment. If you don't know the answer to a question you may write 'skip' as the answer.") 
start=str(input("Are you ready to start(yes/no):"))
correctAnswers=0
incorrectAnswers=0
skips=0
counter=0
questionList=[]
repeat=0

#starting the quiz, displaying the questions in a random order, and collecting user input to the questions
if start=="no":
    print("\nRun this program when you are feeling up to the challenge!")
elif start=="yes":
    while repeat<1:
        askRepeat=0
        while counter<12:
            question=random.randint(1, 12)
            if question==1:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    answer=str(input("\n\nGive one example of an organelle that a plant cell has that an animal cell does not:"))
                    if answer=="cell wall" or answer=="chloroplast":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+4
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1
                                
            if question==2:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    answer=str(input("\n\nThe mule is the offspring of two different species: the donkey and the _____:"))
                    if answer=="horse":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+4
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1
                        
            if question==3:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    answer=str(input("\n\nHumans consume both plants and other animals in order to survive. They take the nutrition and use it to function. What type of consumer are they:"))
                    if answer=="omnivore":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+4
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1

            if question==4:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    answer=str(input("\n\nHow many hearts does an octopus have:"))
                    if answer=="3" or answer=="three":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+4
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1
                        
            if question==5:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    print("\n\nThe Oxpecker is a bird who lands on elephants and eats ticks or other bugs off their backs. The Oxpecker finds food while the elephant gets rid of pests. What type of symbiotic relationship is this:")
                    print("A.)Commensalism")
                    print("B.)Parasitism")
                    print("C.)Mutualism")
                    print("D.)Corrituism")
                    answer=str(input("Enter your answer using the corresponding letters here:"))
                    if answer=="c":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+5
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1
                        
            if question==6:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    print("\n\nTo prepare for hibernation, how much food does a bear eat each day:")
                    print("A.)40kg")
                    print("B.)90kg")
                    print("C.)30kg")
                    print("D.)10kg")
                    answer=str(input("Enter your answer using the corresponding letters here:"))
                    if answer=="a":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+5
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1

            if question==7:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    print("\n\nWhich of these species is the most common household pet:")
                    print("A.)Hamster")
                    print("B.)Cat")
                    print("C.)Dog")
                    print("D.)Fish")
                    answer=str(input("Enter your answer using the corresponding letters here:"))
                    if answer=="d":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+5
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1

            if question==8:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    print("\n\nThe lion lives in grasslands or savannas, where they are uncontested as the king of the land. They have no predators as all others fear the lion. What part of the food chain (trophic level) are they:")
                    print("A.)Primary producers")
                    print("B.)Primary consumers")
                    print("C.)Decomposers")
                    print("D.)Apex predator")
                    answer=str(input("Enter your answer using the corresponding letters here:"))
                    if answer=="d":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+5
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1

            if question==9:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    print("\n\nMushrooms break down dead organic matter and return these nutrients back into soil while creating food for itself. What part of the food chain (trophic level) are they:")
                    print("A.)Primary producers")
                    print("B.)Primary consumers")
                    print("C.)Decomposers")
                    print("D.)Apex predator")
                    answer=str(input("Enter your answer using the corresponding letters here:"))
                    if answer=="c":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+5
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1

            if question==10:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    answer=str(input("\n\nThe cheetah is the fastest animal in the animal kingdom. True or false:"))
                    if answer=="false":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+3
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1

            if question==11:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    answer=str(input("\n\nHoney bees can flap their wings 200 times a second. True or false:"))
                    if answer=="true":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+3
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1

            if question==12:
                if question in questionList:
                    counter=counter+0
                else:
                    questionList.insert(0, question)
                    answer=str(input("\n\nA polar bear has black skin. True or false:"))
                    if answer=="true":
                        print("\nCorrect!")
                        correctAnswers=correctAnswers+3
                        counter=counter+1
                    elif answer=="skip":
                        skips=skips+1
                        counter=counter+1
                    else:
                        print("\nIncorrect.")
                        incorrectAnswers=incorrectAnswers+1
                        counter=counter+1
                        
        #calculating the grade and percentage of the total points
        percentage=correctAnswers/50*100
        if percentage>90:
            grade="A"
        elif percentage>80:
            grade="B"
        elif percentage>70:
            grade="C"
        elif percentage>60:
            grade="D"
        else:
            grade="F"
        #printing correct answers, skips, incorrect answers, percentage of questions answered correctly and a letter grade.                
        print("\n\nYou got", correctAnswers,"points out of 50.")
        print("You got %.2f"% percentage,"%, which is a "+grade)
        print("You skipped", skips,"questions.")
        print("You got", incorrectAnswers,"questions wrong.")

        #asking user if they want to repeat the quiz
        while askRepeat<1:
            answer=str(input("Would you like to repeat the quiz? yes/no:"))
            if answer=="yes":
                repeat=repeat+0
                counter=0
                questionList=[]
                skips=0
                correctAnswers=0
                incorrectAnswers=0
                askRepeat=askRepeat+1
            elif answer=="no":
                repeat=repeat+1
                askRepeat=askRepeat+1
            else:
                askRepeat=askRepeat+0
                     
else:
    print("Enter a valid answer please.")

          
