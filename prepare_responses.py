import yaml

responses_data = {"utter_ask_question": [{"text": "Sure, I can help with that. What would you like to know?"}]}

with open("domain.yml", "a") as file:
    yaml.dump({"responses": responses_data}, file)



