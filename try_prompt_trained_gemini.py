import google.generativeai as genai
from actions import get_response_time
from prompts import system_prompt, user_prompt
from json_helpers import extract_json
from retrieve_trained_model import retrieve_trained_model
import time
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


def generate_text_with_conversation(messages, model_name = "gemini-1.5-flash"):
    
    model = genai.GenerativeModel(model_name=model_name, system_instruction=messages["system_prompt"])
    chat = model.start_chat()
    # Send the user prompt as a message
    response = chat.send_message(messages["user_prompt"])

    # Access the generated response
    generated_text = response.text

    # return response.choices[0].message.content
    return generated_text, chat


#Available actions are:
available_actions = {
    "get_response_time": get_response_time
}

messages = {"system_prompt": system_prompt,
    "user_prompt": user_prompt}


turn_count = 1
max_turns = 3
MODEL_NAME = config.get('model', 'MODEL_NAME')

print(f"\nUser: {messages['user_prompt']}")

while turn_count < max_turns:
    print (f"\nLoop: {turn_count}")
    print("----------------------")

    request_failed = True
    while request_failed:
        try:
            if turn_count == 1:
                chat = retrieve_trained_model()
                response = chat.send_message(messages["system_prompt"])            
                response = chat.send_message(messages["user_prompt"])
                response = response.text
            else:
                response = chat.send_message(messages["user_prompt"])
                # Access the generated response
                response = response.text
            request_failed = False
        except Exception as e:
            if 'quota' not in str(e):
                raise Exception(f"Failed to retrieve model: {e}")
            print("Error occured:", e)
            print("request failed.... waiting for 1 minutes due to quota limitations")
            time.sleep(60)
            

    turn_count += 1

    print("Model Response:")
    print(response)
    json_function = extract_json(response)

    if json_function:
        print("jsonized response:")
        print(json_function)
        function_name = json_function[0]['function_name']
        function_parms = json_function[0]['function_parms']
        if function_name not in available_actions:
            raise Exception(f"Unknown action: {function_name}: {function_parms}")
        print(f" -- running {function_name} {function_parms}")
        action_function = available_actions[function_name]
        #call the function
        result = action_function(**function_parms)
        function_result_message = f"({function_parms}) - Action_Response: {result}"
        messages["user_prompt"] = function_result_message
        print(function_result_message)
    else:
         break
