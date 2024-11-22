# Install the client library and import necessary modules.
import google.generativeai as genai
import base64
import copy
import json
from content.model_content import content, generation_config_b64
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

def retrieve_trained_model():

    # Configure the client library by providing your API key.
    GEMINI_API_KEY = config.get('model', 'GEMINI_API_KEY')    

    genai.configure(api_key=GEMINI_API_KEY)
    model = config.get('model', 'MODEL_NAME') # @param {isTemplate: true}
    contents_b64 = content # @param {isTemplate: true}
    safety_settings_b64 = "e30="  # @param {isTemplate: true}

    gais_contents = json.loads(base64.b64decode(contents_b64))

    generation_config = json.loads(base64.b64decode(generation_config_b64))
    safety_settings = json.loads(base64.b64decode(safety_settings_b64))
    contents = copy.deepcopy(gais_contents)


    """## Create a chat"""

    gemini = genai.GenerativeModel(
        model_name=model,
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    """A `ChatSession`, should always end with the model's turn.

    So before creating the `chat` check whos turn was last.

    If the user was last, attach all but the last content as the `history` and send the last content with `send_message` to get the model's response.

    If the model was last, put the whole contents list in the history.
    """
    print("Retrieving trained model...")
    model_turn = contents[-1].get("role", None) == "user"

    if model_turn:
        chat = gemini.start_chat(history=contents[:-1])

        response = chat.send_message(contents[-1])

        if generation_config.get("candidate_count", 1) == 1:
            # display(Markdown(response.text))
            print(response.text)
    else:
        chat = gemini.start_chat(history=contents)

    if model_turn:
        response.candidates

    print("model retrieved successfully!")
    return chat

