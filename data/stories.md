## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## diagnosis path 1

* greet
    - utter_greet
* need_help
    - utter_help
* symptom
    - action_handle_symptom
* deny
    - utter_alternative
* symptom
    - action_handle_symptom
* deny
    - utter_alternative
* symptom
    - action_handle_symptom
* deny
    - utter_alternative
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

## New Story

* greet
    - utter_greet
* need_help
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
* symptom
    - action_handle_symptom
* end
    - action_diagnosis
* end
    - action_diagnosis

## New Story

* greet
    - utter_greet
* need_help
    - utter_help
* symptom
    - action_handle_symptom
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
* symptom
    - action_handle_symptom
* symptom
    - utter_alternative
* symptom
    - action_handle_symptom
* end
    - action_diagnosis

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* end
    - action_diagnosis

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye
* end
    - action_diagnosis

## say goodbye
* goodbye
  - utter_goodbye
* end
    - action_diagnosis

## bot challenge
* bot_challenge
  - utter_iamabot
* end
    - action_diagnosis
