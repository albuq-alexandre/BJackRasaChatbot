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

class SubmitAgendamento(Action):

	def name(self) -> Text:
		return "action_submit_agendamento"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#recebe dados dos slots
		cidade = tracker.get_slot('cidade')
		data = tracker.get_slot('data')

		d = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f%z')
		convert_data = d.strftime('%d/%m/%Y às %H:%M')
		#executa alguma coisa com os dados

		#limpa slots do agendamento
		return [
			SlotSet('resultado_cidade', cidade), 
			SlotSet('resultado_data', convert_data), 
			SlotSet('cidade', None),
			SlotSet('data', None)
			]
