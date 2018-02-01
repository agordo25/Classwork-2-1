#trivia quiz

print("This is a quiz that tests yor knowledge on _______")

name=input("enter your name")
print("Hi there,",name, "Are you ready to start the quiz?")


print("I will ask you 6 questions and give you three choices")
print("Select which choice is the correct answer, A, B, or C")

#set the score of the quiz to 8
score = 0
score = int(score)

#question 1
print("Question 1: What is the largest ocean in the world? /n")

print("A. The Indian Ocean")
print("B. The Pacific Ocean")
print("C. The Atlantic Ocean")
print("")

Q1answer="B"#the right answer to question 1
Q1response=input("Your answer:")

if Q1response == "B" or Q1response == "b":
    print("Correct answer", Q1response)
    score= score+1
elif Q1response != "B" or Q1response != "b":
    print("Sorry, incorrect")

print("Your current score is",score,"out of 6") 

#percentage score
final_score=(score*100)/6
print("This is a score of" + str(final_score),"percent")
