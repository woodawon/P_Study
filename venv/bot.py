from chatterbot import ChatBot
chatbot = ChatBot("Chatbot")
exit_conditions = (":q", "quit", "exit") # tuple

while True:
    query = input("> ")
    if query in exit_conditions: # 3개중에 하나라도 해당되면
        break
    else:
        print(f"{chatbot.get_response(query)}")