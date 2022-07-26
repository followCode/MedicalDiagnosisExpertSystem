# MedicalDiagnosisExpertSystem

```
**DISCLAIMER**
This project isn't meant to be used as a primary source of medical advice and it is recommended that the user consult a doctor before moving ahead with any decisions. The bot isn't a hundred percent accurate and can make mistakes, so any action taken by
the user without consulting a trained physician is at the users own discretion. The project developers and the project itself are not to be blamed for the decisions taken by the user based on the conversation with the chatbot.
```

### Goal of project
To be able to build a simple expert system which provides medical diagnosis for common ailments.
This expert system allows us to handle user input through a chatbot type interface. It takes the symptoms from the user interactively and uses that for predicting the diseases.

### Overview
- Intent Recognition
  - Using Rasa NLU, the “intent” of the user’s input is recognized. This is done using supervised learning system defined in the Rasa Pipeline

- Model
  - The symptoms given as input are lemmatized so as to make it understandable to the mode and stored in a vector.
  - Using KNN, the model identifies nearby symptoms for the given set of symptoms.

- Conversation Flow - Stories
  - Conversations are defined as different forms using Stories in Rasa. Using stories, the bot handles responses and checking for intent

- Bot Memory/Slots
  - This is a mechanism in Rasa that allows the bot to store User responses in memory for use by other actions.

- Rasa Actions
  - Based on user response and “slot” information collected from previously in the conversation, the bot can take actions such as responding, showing options,etc.

### Setup
- Install the requirements:
```bash
$ pip install -r requirements.txt
```

- Install Rasa-X
```bash
$ pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

- Download spacy base

```bash
$ python -m spacy download en_core_web_md
$ python -m spacy link en_core_web_md en
```

- Train the Rasa conversational model

```bash
$ rasa train
```

### Run

1. Run the action server (endpoint)
```bash
$ rasa run actions
```

2. Start the Rasa X instance to chat with bot
```bash
$ rasa x
```

### Output

1. Initiation of conversation

![alt text](https://github.com/followCode/MedicalDiagnosisExpertSystem/raw/master/images/init.jpeg "Initiation of the conversation")

2. Stepping through the conversation

![alt text](https://github.com/followCode/MedicalDiagnosisExpertSystem/raw/master/images/step1.jpeg "Stepping in conversation")

3. Providing diagnosis for the symptoms

![alt text](https://github.com/followCode/MedicalDiagnosisExpertSystem/raw/master/images/step2.jpeg "Stepping into conversation")

