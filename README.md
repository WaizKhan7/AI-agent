# AI Agent Demo: Using Gemini Model and Function Calling Feature

This repository demonstrates how to use **Google's Gemini LLM model** with features like **function calling** and **importing prompt-engineered models** to build powerful, interactive AI agents.  

The codebase is modular and customizable, allowing you to adapt the behavior and context of the AI by modifying key components like prompts and chat history.  



## **Features**

1. **Gemini Model Integration**:
   - Learn how to connect and interact with Google's Gemini model API.  
   - Use any `gemini` model to generate responses and chat with your AI agent.
2. **Function Calling with LLMs**:
   - Explore the "function calling" feature to execute predefined actions based on the AI's reasoning.
3. **Prompt Engineering**:
   - Understand how to guide the AI's behavior with carefully designed prompts.
   - Use the `prompts.py` file to set instructions, available actions, and examples for the AI agent.
4. **Importing Prompt-Engineered Models**:
   - Learn how to retrieve and use a **prompt-engineered trained model** from Google AI Studio.
   - Save and reuse chat history or prompts for advanced customization using `content/model_content.py`.



## **Repository Overview**

The repository is organized into modular files to make it easy to customize and extend the AI agent.

### **How to Use and Customize**

You can use this repo to build AI Agent for any uses case. Below are the details about the each file, and how you can edit them for your use.

1. **`config.ini`**
   - Add `GEMINI_API_KEY`, you can get one from https://aistudio.google.com.
   - Add `MODEL_NAME` i.e.  `gemini-1.5-flash` or `gemini-1.5-pro`.
2. **`model_content.py`**:
   - Stores raw prompt/chat history or data for prompt-engineered models, useful for initializing a chat context.
   - If you have a prompt-trained Gemini model, provide `content` and `generation_config_b64` values from the `Get Code` option.
3. **`prompts.py`**:
   - Contains the system's instructions and examples for interaction.  
   - You can edit `system_prompt` to define the AI's role, working style, and available actions.  
   - Update `user_prompt` to set the initial query for the AI.
4. **`actions.py`**:
   - Contains implementations for the available actions (e.g., `get_response_time`).
   - Extend this file to add more actions and functionalities.
5. **`main.py`**:
   - Demonstrates how to use the Gemini model to process user queries and execute actions via function calling.
   - Includes a structured loop where the AI thinks, acts, pauses for results, and provides an answer.
6. **`try_prompt_trained_gemini.py`**:
   - Shows how to load and use a **trained prompt-engineered model**.
   - Implements functionality to reuse trained models for generating consistent and improved responses.

### **Prerequisites**

1. Python 3.10 or higher.  

2. A Gemini API Key to use the `google generative ai` library.  

3. Install the required Python packages by running:

   ```bash
   pip install "google-generativeai>=0.8.2"
   ```

   

### **Quick Start**

1. Clone the repository:

   ```
   git clone https://github.com/WaizKhan7/AI-agent.git
   cd AI-agent
   ```

2. Set values for `GEMINI_API_KEY` and `MODEL_NAME` you want to use i.e. `gemini-1.5-flash` or `gemini-1.5-pro`.

3. Run `main.py` to interact with the AI agent:

   ```
   python3 main.py
   ```

4. To use a trained prompt-engineered model, set `content.model_content.py` file and run:

   ```
   python3 try_prompt_trained_gemini.py
   ```



## **Sample Output**

````
User: what is the response time of url 'github.com/WaizKhan7'?

Loop: 1
----------------------
Model Response:
Thought: I need to determine the response time for the given URL.  I'll use the `get_response_time` function.

Action:

```json
{
  "function_name": "get_response_time",
  "function_parms": {
    "url": "github.com/WaizKhan7"
  }
}
```

PAUSE

 -- running get_response_time {'url': 'github.com/WaizKhan7'}
({'url': 'github.com/WaizKhan7'}) - Action_Response: 0.2

Loop: 2
----------------------
Model Response:
Thought:The Action_Response provides the response time for the given URL.  I can now formulate an answer.

Answer: The response time for github.com/WaizKhan7 is 0.2 seconds.
````



## **Limitations**

1. **API Quota**: The Gemini model may have usage limits or quotas. Use sleep intervals in loops to avoid errors.
2. **Error Handling**: Ensure robust handling for invalid JSON, unexpected function calls, or API request failures.
3. **Customization Effort**: Users need to modify prompts and actions according to their specific use cases.



## **Future Improvements**

- Add more predefined actions and extend functionality.
- Integrate with other APIs or services for enhanced interactivity.
- Provide a web-based interface for easier interaction with the AI agent.