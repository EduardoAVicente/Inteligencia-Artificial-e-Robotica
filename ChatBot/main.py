from chatbot import ChatBot
myChatBot = ChatBot()
import os
#apenas carregar um modelo pronto
myChatBot.loadModel()

#criar o modelo
# myChatBot.createModel()


username = os.getlogin()

os.system('cls')
print("Bem vindo ao Chatbot")


print("como posso te ajudar? ")
pergunta = input(username + ": ")
print()
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")
print()


while (intencao[0]['intent']!="despedida"):
    print("posso lhe ajudar com algo a mais?")
    pergunta = input(username + ": ")
    print()
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")
    print( )
print("Foi um prazer atendê-lo")
