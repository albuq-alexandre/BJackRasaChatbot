# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset

import datetime
import jsonpickle
import logging
from .game import BlackJackGame

#configura logging e config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('BJackRasaActions')
#

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ClearSlots(Action):

	def name(self) -> Text:
		return "action_clear_slots"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#limpa slots do agendamento
		return [AllSlotsReset()]

# - action_clear_slots
# - action_submit_agendamento
# - action_iniciar
# - action_mais1carta
# - action_parar
# - action_terminar
# - action_listar
# - action_estatística

class Iniciar(Action):

	def name(self) -> Text:
		return "action_iniciar"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#recebe dados dos slots
		gameJson = tracker.get_slot('game')
		nome = tracker.get_slot('nome_gamer')
		if not gameJson:
			game = BlackJackGame()
		else:
			game = jsonpickle.decode(gameJson)
		if not nome:
			game.players[1].name = nome
		#executa o início do jogo
		txt_values, return_values_img = game.start(audible = False)
		logger.info(return_values_img)

		dispatcher.utter_message(text="Cartas na Mesa!")
		dispatcher.utter_message(text=return_values_img)

		return [
			SlotSet('game', jsonpickle.encode(game)),
			SlotSet('resultado_nome_gamer', nome),
			SlotSet('nome_gamer', None)
			]

class Pegar_carta(Action):

	def name(self) -> Text:
		return "action_mais1carta"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#recebe dados dos slots
		gameJson = tracker.get_slot('game')

		if not gameJson:
			dispatcher.utter_message("Jogo não iniciado...\nBora jogar Blackjack?")
			return []
		else:
			game = jsonpickle.decode(gameJson)

			#executa o pegar mais uma carta no jogo
			txt_values, return_values_img = game.draw_card(audible = False)
			dispatcher.utter_message(text="Cartas na Mesa!")
			dispatcher.utter_message(text=return_values_img)

		return [
			SlotSet('game', jsonpickle.encode(game))
			]

class Parar(Action):

	def name(self) -> Text:
		return "action_parar"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#recebe dados dos slots
		gameJson = tracker.get_slot('game')

		if not gameJson:
			dispatcher.utter_message("Jogo não iniciado...\nBora jogar Blackjack?")
			return []
		else:
			game = jsonpickle.decode(gameJson)

			#executa o parar o jogo e avaliar o resultado
			if game.running:
				game.dealers_turn(audible=False)
			txt_values, return_values_img = game.evaluate(audible = False)
			dispatcher.utter_message(text="Cartas na Mesa!")
			dispatcher.utter_message(text=return_values_img)
			dispatcher.utter_message(text=txt_values)

		return [
			SlotSet('game', jsonpickle.encode(game))
			]

class Terminar(Action):

	def name(self) -> Text:
		return "action_terminar"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#recebe dados dos slots
		gameJson = tracker.get_slot('game')

		if not gameJson:
			dispatcher.utter_message("Jogo não iniciado...\nBora jogar Blackjack?")
			return []
		else:
			game = jsonpickle.decode(gameJson)

			#executa o parar o jogo e avaliar o resultado
			ret = ''
			for player in game.players:
				ret = ret + "<b>" + player.name + "</b>\n"
				ret = ret + player.list_matches() + '\n'
				ret = ret + player.stats(audible=False) + '\n'
			return_values_img = ret
			game.terminate()
			dispatcher.utter_message(text="Cartas na Mesa!")
			dispatcher.utter_message(custom=return_values_img, parse_mode='html')
			dispatcher.utter_custom_json({'text': return_values_img, 'parse_mode': 'html'})

		return [
			SlotSet('game', jsonpickle.encode(game))
			]

class Listar(Action):

	def name(self) -> Text:
		return "action_listar"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#recebe dados dos slots
		gameJson = tracker.get_slot('game')

		if not gameJson:
			dispatcher.utter_message("Jogo não iniciado...\nBora jogar Blackjack?")
			return []
		else:
			game = jsonpickle.decode(gameJson)

			#lista as partidas do Player
			return_values_img = game.players[1].list_matches()
			dispatcher.utter_message(text="Partidas do Jogador - " + game.players[1].name)
			dispatcher.utter_message(text=return_values_img)

		return [
			SlotSet('game', jsonpickle.encode(game))
			]

class Estatistica(Action):

	def name(self) -> Text:
		return "action_estatistica"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#recebe dados dos slots
		gameJson = tracker.get_slot('game')

		if not gameJson:
			dispatcher.utter_message("Jogo não iniciado...\nBora jogar Blackjack?")
			return []
		else:
			game = jsonpickle.decode(gameJson)
			#lista as partidas do Player
			return_values_img = game.players[1].stats(audible = False)
			dispatcher.utter_message(text=return_values_img)

		return [
			SlotSet('game', jsonpickle.encode(game))
			]
