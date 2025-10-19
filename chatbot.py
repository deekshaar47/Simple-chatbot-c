print("chatbot:Hello! I am your friendly chatbot.Type 'bye'to exit.")
while True:
    user_input=input("you: ").lower()
    if user_input in["hi","hii","hello","hey"]:
        print("chatbot:Heloo there !How can I help you today?")
    elif user_input in["how are you","how are you?"]:
        print("chatbot:I'm just program,but i a'm doing great!how about you?")
    elif   "your name"in user_input:
        print("chatbot:My name is pyBot,created by Deeksha!")
    elif "weather" in user_input:
        print("chatbot:i can't check the weather yet,but you can try my weather app")
    elif "time" in user_input:
        from datetime import datetime
        print("chatbot:current time is",datetime.now().strftime("%H:%M:%S"))
    elif "bye" in user_input:
        print("chatbot:GoodBye!Have a grate day,Deeksha!")
        break
    else:
        print("chatbot:Sorry! I didn't understand taht.can you rephrase?")

