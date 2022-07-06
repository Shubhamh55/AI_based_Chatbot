from  chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

myBot = ChatBot(name='PyBot', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

