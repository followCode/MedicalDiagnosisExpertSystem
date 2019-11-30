## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## diagnosis path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_help
* symptom
  - action_handle_symptom
* deny
  - utter_alternative
* symptom
  - action_handle_symptom
* symptom
  - action_handle_symptom
* deny
  - utter_alternative
* symptom
  - action_handle_symptom
* deny
  - utter_alternative
* deny
  - action_diagnosis

## diagnosis path 2
* greet
    - utter_greet
* mood_unhappy
    - utter_help
* symptom
    - action_handle_symptom
* deny
    - utter_alternative
* symptom
    - action_handle_symptom
* symptom
    - action_handle_symptom
* deny
    - utter_alternative
* symptom
    - action_handle_symptom
* deny
    - utter_alternative
* end
    - action_diagnosis
    - utter_did_that_help

## diagnosis path 2
* greet
    - utter_greet
* mood_unhappy
    - utter_help
* symptom
    - action_handle_symptom
* symptom
    - action_handle_symptom
* symptom
    - action_handle_symptom
* symptom
    - action_handle_symptom
* symptom
    - action_handle_symptom
* end
    - action_diagnosis
    - utter_did_that_help