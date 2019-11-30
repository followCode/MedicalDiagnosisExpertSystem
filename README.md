# MedicalDiagnosisExpertSystem

```
**DISCLAIMER**
This project isn't meant to be used as a primary source of medical advice and it is recommended that the user consult a doctor before moving ahead with any decisions. The bot isn't a hundred percent accurate and can make mistakes, so any action taken by
the user without consulting a trained physician is at the users own discretion. The project developers and the project itself are not to be blamed for the decisions taken by the user based on the conversation with the chatbot.
```

### Goal of project
To be able to build a simple expert system which provides medical diagnosis for common ailments.
Using a chatbot was only trivial as it serves as the best approach to interact with users in the current age of the Internet.

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

