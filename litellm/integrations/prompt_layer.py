#### What this does ####
#    On success, logs events to Promptlayer
import dotenv, os
import requests
import requests

dotenv.load_dotenv()  # Loading env variables using dotenv
import traceback

class PromptLayerLogger:
    # Class variables or attributes
    def __init__(self):
        # Instance variables
        self.key = os.getenv("PROMPTLAYER_API_KEY")

    def log_event(self, kwargs, response_obj, start_time, end_time, print_verbose):
        # Method definition
        try:
            print_verbose(
                f"Prompt Layer Logging - Enters logging function for model {kwargs}"
            )

            request_response = requests.post(
                "https://api.promptlayer.com/rest/track-request",
                json={
                    "function_name": "openai.ChatCompletion.create",
                    "kwargs": kwargs,
                    "tags": ["hello", "world"],
                    "request_response": dict(response_obj), # TODO: Check if we need  a dict
                    "request_start_time": int(start_time.timestamp()),
                    "request_end_time": int(end_time.timestamp()),
                    "api_key": self.key,
                    # Optional params for PromptLayer
                    # "prompt_id": "<PROMPT ID>",
                    # "prompt_input_variables": "<Dictionary of variables for prompt>",
                    # "prompt_version":1,

                },
            )

            print_verbose(f"Prompt Layer Logging - final response object: {request_response}")
        except:
            # traceback.print_exc()
            print_verbose(f"Prompt Layer Error - {traceback.format_exc()}")
            pass
