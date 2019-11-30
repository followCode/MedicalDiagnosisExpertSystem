# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
#         dispatcher.utter_message("Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random
from helper import Diagnosis

dObj = Diagnosis()
dObj.train()

suggested_so_far = []

class ActionHandleSymptom(Action):

    def name(self) -> Text:
        return "action_handle_symptom"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get the last message sent by user
        message = tracker.latest_message.get('text')

        # Get symptoms slot
        syms = tracker.get_slot("symptom_list")

        if syms is None:
            syms = []

        # Check if symptom in list
        if message not in syms:
            syms.append(message)
        else:
            dispatcher.utter_message("Already noted that you have: "+message)
            return []
        
        # Update slot
        SlotSet("symptom_list", syms)

        # Get suggested symptom based on input
        suggested_symptom = dObj.suggest_symptoms(syms)
        
        # Check if symptom not already suggested
        clean_syms=[]

        for symp in suggested_symptom:
            if symp not in syms and symp not in suggested_so_far:
                clean_syms.append(symp)
            else:
                suggested_so_far.append(symp)

        if(len(clean_syms)>0):
            num = random.randrange(0,len(clean_syms))
        else:
            dispatcher.utter_template('utter_alternative')
            return [SlotSet("symptom_list", syms)]

        # Create response buttons
        buttons = [{"title": "Yes", "payload": clean_syms[num]},{"title":"No", "payload": "/deny"}]

        # Send message
        dispatcher.utter_message("You said you have: "+message)
        dispatcher.utter_button_message("Do you also have "+clean_syms[num]+"?", buttons)

        return [SlotSet("symptom_list", syms)]

class ActionDiagnosis(Action):

    def name(self) -> Text:
        return "action_diagnosis"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get symptoms slot
        syms = tracker.get_slot("symptom_list")

        # Get diagnosis
        diag = dObj.predict(syms)

        print(diag)

        # Send message
        dispatcher.utter_message("Our Diagnosis: "+str(diag[0]))
        dispatcher.utter_message("Suggested medication:")
        for d in str(diag[1]).split(","):
            dispatcher.utter_message(str(d))
            dispatcher.utter_message("["+str(d)+"](https://www.1mg.com/search/all?name="+(str(diag[1]).split(',')[0])+")")

        dispatcher.utter_message("Suggested Doctor: ")
        dispatcher.utter_message("[Go here](https://www.practo.com/search/findDoc?name="+diag[0]+")")

        return []


        
