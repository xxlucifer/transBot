from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# I used a simulated database for now, as you suggested in the mail.
database = {
            "Alina": {
                "account_number": "12345",
                "balance": 15500,
                "transactions":{"Paid Rs.200 to Kirana Store.",
                                "Paid Rs. 420 to Pathao.",
                                "Received Rs.2000 from Ramesh."}
                },
            "Ramesh": {
                "account_number": "11111",
                "balance": 223000,
                "transactions":{"Paid Rs.2000 to Oliz Store.",
                                "Paid Rs. 20000 to Trisara."}
                },
            "Chaurey": {
                "account_number": "22222",
                "balance": 25900,
                "transactions":{"Paid Rs.25 to Kirana Store.",
                                "Paid Rs. 160 to Dairy.",
                                "Received Rs.5000 from Ramesh."}
                
            }}
        

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        
        name = tracker.get_slot("name")
        account_number = tracker.get_slot("account_number")
        
        if name in database and account_number == database[name]["account_number"]:
            balance = database[name]["balance"]
            response = f"Dear {name}, your account {account_number} has a balance of Rs. {balance}."
        else:
            response = " Please make sure you gave me your credentials(name, acc number, phone number) & they are correct."
        
        dispatcher.utter_message(response)
        
        return []

class ActionTransactionHistory(Action):
    def name(self) -> Text:
        return "action_transaction_history"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        account_number = tracker.get_slot("account_number")
        
        if name in database and account_number == database[name]["account_number"]:
            transactions = database[name]["transactions"]
            response = f"Sure, {name}, I will show you your transaction history: {transactions}"
        else:
            response = "I need your name and account number to access your transaction history."
        
        dispatcher.utter_message(response)
        
        return []