from chatBot import chatBot
while(1):
    query=input("Enter query")
    response = chatBot.chatbot_response(query)
    print(response)