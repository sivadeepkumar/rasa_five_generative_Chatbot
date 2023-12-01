# from my_html_parser import qna_data

# import yaml

# training_data = {"version": "2.0", "nlu": []}

# for intent, examples in qna_data.items():
#     training_data["nlu"].append({"intent": intent+"_intent_name", "examples": intent})

# with open("data/nlu.yml", "w") as file:
#     yaml.dump(training_data, file)

from my_html_parser import qna_data
import yaml
import pprint
training_data = {"version": "2.0", "nlu": []}
responses_data = {}
stories_data = {}
count = 0
for heading, examples in qna_data.items():
    # Add intent data to training_data
    intent = "intent_"+str(count)
    training_data["nlu"].append({"intent": intent, "examples": heading})
    pprint.pprint(training_data)
    # Prepare response data
    utter = "utter_" + str(count)
    responses_data[utter] = [{"text": examples}]
    # pprint.pprint(responses_data)
    # Prepare stories data
    stories_data["AskQuestion_"+str(count)] = [{"intent": intent}, {"action": utter}]
    count += 1
    # pprint.pprint(stories_data)



# # Save training data to nlu.yml
# with open("data/nlu.yml", "w") as file:
#     yaml.dump(training_data, file)

# # Save response data to domain.yml
# with open("domain.yml", "a") as file:
#     yaml.dump({"responses": responses_data}, file)

# # Save stories data to stories.yml
# with open("data/stories.yml", "a") as file:
#     yaml.dump({"stories": stories_data}, file)



