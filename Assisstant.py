
import datetime
import time

name = input('Swagat h, enter your name :')
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning",name)
elif 11 <= presentHour <=17:
    print("Good afternoon",name) 
elif 17 <= presentHour <= 20:
    print("Good evening",name)
else:
    print("Good night",name)           

print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question,Type 'Bye' to exit from the Bot")
 #Chatbot memory creation[dictionary of responses]
responses = {
    "hello":"Hii ,Welcome.How can I help you?",
     "how are you":"I am very fine.Thank you",
     "who are you":"I am smart AI chatbot",
     "motivate me":"Keep going.Every bug of your project makes you a better developer",
     "happy":"Great to hear that",
     "functions kya hote h ":"jakar chapter 7 padho"
    }
#Method /function to get response of chatbot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell thet yet.I am still in learning mode."    
#Take user input
while True:
    userInput = input("Please ask your questions:")
    reply = getResponseOfBot(userInput)
    print("Bot Response :",reply)

    if "bye" in userInput.lower():
       break 