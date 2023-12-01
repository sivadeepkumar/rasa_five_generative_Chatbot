import yaml

stories_data = {"Ask Question": [{"intent": "ask_question"}, {"action": "utter_ask_question"}]}

with open("data/stories.yml", "a") as file:
    yaml.dump({"stories": stories_data}, file)




